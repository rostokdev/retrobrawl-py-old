from packets.Messages import Message
from packets.Messages.Server.UnlockAccountFailedMessage import UnlockAccountFailedMessage
from packets.Messages.Server.UnlockAccountOkMessage import UnlockAccountOkMessage
from database.cods import *

class UnlockAccountMessage(Message):
	def __init__(self, player):
		super().__init__()
		self.id = 10121
		self.player = player
		self.db = DataBaseCods()

	def decode(self, buffer):
		super().decode(buffer)
		self.readInt32()
		self.readInt32() 

		self.readString()
		self.code = self.readString()

	def process(self):
		dbData = self.db.get_code_db(self.code)
		#print(self.code, dbData)
		if (dbData != []):
			self.db.delete_code_db(self.code)
			UnlockAccountOk_Message = UnlockAccountOkMessage(self.player)
			UnlockAccountOk_Message.encode()
			UnlockAccountOk_Message.encode()
			UnlockAccountOk_Message.buffer = self.player.clientsAll["players"][str(self.player.LowID)]["crypto"].encrypt(UnlockAccountOk_Message.id, UnlockAccountOk_Message.buffer)
			UnlockAccountOk_Message.pack()
			self.player.DataDB["access"] = True
			self.player.setData()
		else:
			UnlockAccountOk_Message = UnlockAccountFailedMessage()
			UnlockAccountOk_Message.encode()
			UnlockAccountOk_Message.encode()
			UnlockAccountOk_Message.buffer = self.player.clientsAll["players"][str(self.player.LowID)]["crypto"].encrypt(UnlockAccountOk_Message.id, UnlockAccountOk_Message.buffer)
			UnlockAccountOk_Message.pack()

		self.buffer = UnlockAccountOk_Message.buffer
