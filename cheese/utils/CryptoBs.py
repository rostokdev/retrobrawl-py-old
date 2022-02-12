from os import urandom
from hashlib import blake2b
from _tweetnacl import (crypto_box_afternm,crypto_box_beforenm,crypto_scalarmult_base,crypto_box_open_afternm, crypto_box_NONCEBYTES, crypto_hash, crypto_secretbox, crypto_secretbox_open)

class Nonce:
	def __init__(self, nonce=None, clientKey=None, serverKey=None):
		if not clientKey:
			if nonce:
				self._nonce = nonce
			else:
				self._nonce = urandom(crypto_box_NONCEBYTES)
		else:
			b2 = blake2b(digest_size=24)
			if nonce:
				b2.update(bytes(nonce))
			b2.update(bytes(clientKey))
			b2.update(serverKey)
			self._nonce = b2.digest()
	def __bytes__(self):
		return self._nonce
	def __len__(self):
		return len(self._nonce)
	def increment(self):
		self._nonce = (int.from_bytes(self._nonce, 'little') + 2).to_bytes(crypto_box_NONCEBYTES, 'little')
                                        
class CryptoBs:
	def __init__(self, server_key, device):
		self.device = device
		self.server_key = bytes.fromhex("78BD03628030B86BCF17817DF13A3E9C0E8FD03F06F222A44C40CA70F3ECC748")
		self.client_sk = bytes.fromhex("85980ab6075cc197ab8de0faba3c699682b459979365435144482f5ebae82145")
		self.client_pk = crypto_scalarmult_base(self.client_sk)
		self.session_key = b'\x13Y\xd8\x13M\x19\xf6\xffv\xe7q{\xb0\x9dl\x0c\x81\xe7)(\x9b\t\xc3\xfc'
		self.session_key_is = False
		self.shared_key = None
		self.decryptNonce = None
		self.encryptNonce = Nonce(urandom(24))
		self.shared_en = bytes(urandom(32))
		self.public_key = None
		self.s = None
		self.nonce = None
	
	def decrypt_server(self, packet_id, payload):
		#self.encryptNonce.increment()
		return crypto_secretbox_open(payload, bytes(self.encryptNonce), self.shared_en)
		
	def decrypt(self, packet_id, payload):
		if self.device.state == self.device.StateSession:
			return payload
			
		elif self.device.state == self.device.StateLogin:
			if payload[:32].hex() != self.client_pk.hex():
				print(f"[ERROR] Ошибка криптографии, пакет: {packetID}, client_pk: {self.client_pk}, ключ пакета: {payload[:32]}")
			else:
				self.session_key_is = True
				self.public_key = payload[:32]
				payload = payload[32:]
				self.nonce = Nonce(clientKey=self.client_pk, serverKey=self.server_key)
				self.s = crypto_box_beforenm(self.server_key, self.client_sk)
				decrypted = crypto_secretbox_open(payload, bytes(self.nonce), self.s)
				session_key = decrypted[0:24]
				if session_key != self.session_key:
					print("[ERROR] Ошибка... ключи session_key не совпадают!")
				self.decryptNonce = Nonce(decrypted[24:48]) # decrypted nonce
				return decrypted[48:]
		elif self.device.state == self.device.StateLogged:
			self.decryptNonce.increment()
			decrypted = crypto_secretbox_open(payload, bytes(self.decryptNonce), self.shared_en)
			#print(decrypted)
			return decrypted
		else:
			print(f"[INFO-ERROR-DECRYPT] State {self.device.state} undifined")
					
	def encrypt(self, packetID, payload):
		if self.device.state == self.device.StateSession:
			return payload
		elif self.device.state == self.device.StateLogin:
			print("encrypted: " + str(packetID))
			nonce = Nonce(self.decryptNonce, clientKey=self.client_pk, serverKey=self.server_key)
			payload = bytes(self.encryptNonce) + self.shared_en + payload
			encrypted = crypto_secretbox(payload, bytes(nonce), self.s)
			return encrypted
		elif self.device.state == self.device.StateLogged:
			self.encryptNonce.increment()
			encrypted = crypto_secretbox(payload, bytes(self.encryptNonce), self.shared_en)
			return encrypted
		else:
			print(f"[INFO-ERROR-ENCRYPT] State {self.device.state} undifined")