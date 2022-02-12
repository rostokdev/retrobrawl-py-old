from packets.Messages import Message
from packets.Messages.Server.OwnHomeDataMessage import OwnHomeData
from database.cods import *

class GoHomeFromOfflinePractiseMessage(Message):
	def __init__(self, player):
		super().__init__()
		self.id = 14109
		self.player = player

	def decode(self, buffer):
		super().decode(buffer)

	def process(self):
		ohd = OwnHomeData(self.player)
		ohd.encode()
		ohd.buffer = self.player.clientsAll["players"][str(self.player.LowID)]["crypto"].encrypt(ohd.id, ohd.buffer)
		ohd.pack()
		self.buffer = ohd.buffer
