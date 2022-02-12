from packets.Messages import Message
from packets.Messages.Server.AllianceDataMessage import AllianceDataMessage
import json

class AskForAllianceDataMessage(Message):
	def __init__(self, player):
		super().__init__()
		self.id = 14302
		self.player = player

	def decode(self, buffer):
		super().decode(buffer)
		self.readInt32()
		self.lowid = self.readInt32()

	def process(self):
		dataClub = json.loads(self.player.getAliiance_lowId(self.lowid)[0][1])

		AllianceData_Message = AllianceDataMessage(dataClub)
		AllianceData_Message.encode()
		AllianceData_Message.buffer = self.player.clientsAll["players"][str(self.player.LowID)]["crypto"].encrypt(AllianceData_Message.id, AllianceData_Message.buffer)
		AllianceData_Message.pack()
		self.buffer = AllianceData_Message.buffer
		"""
		AllianceResponse_Message = AllianceResponseMessage(dataClub)
		AllianceResponse_Message.encode()
		AllianceResponse_Message.buffer = self.player.crypto.encrypt(AllianceResponse_Message.id, AllianceResponse_Message.buffer)
		AllianceResponse_Message.pack()
		self.buffer += AllianceResponse_Message.buffer
		"""