from packets.Messages import Message
from utils.reader import Reader
from utils.writer import Writer


class LoginFailedMessage(Message):
	def __init__(self, player, code, reason=""):
		super().__init__()
		self.id = 20103
		self.code = code
		self.player = player
		self.reason = reason

	def decode(self, buffer):
		Reader.__init__(self, buffer)

	def encode(self):
		Writer.__init__(self)
		self.writeInt32(self.code)
		self.writeString()
		self.writeString()
		self.writeString()
		self.writeString()
		self.writeString(self.reason)
		self.buffer += bytes.fromhex('''2E0000012C000000000000000000''')
		self.writeString()
		self.writeString()
		self.writeString()
		self.writeString()
		self.writeVint(0)
	def encrypt(self):
		if (self.player.device.state == self.player.device.StateLogged):
			self.player.device.state = self.player.device.StateLogin 
		self.buffer = self.player.crypto.encrypt(self.id, self.buffer)
		if (self.player.device.state == self.player.device.StateLogin):
			self.player.device.state = self.player.device.StateLogged 