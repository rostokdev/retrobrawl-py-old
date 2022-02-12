from packets.Messages import Message
from packets.Messages.Server.TeamLeftMessage import TeamLeftMessage
from database.cods import *

class TeamLeaveMessage(Message):
	def __init__(self, player):
		super().__init__()
		self.id = 14353
		self.player = player

	def decode(self, buffer):
		super().decode(buffer)

	def process(self):
		TeamLeaveOk_Message = TeamLeftMessage(self.player)
		TeamLeaveOk_Message.encode()
		TeamLeaveOk_Message.buffer = self.player.clientsAll["players"][str(self.player.LowID)]["crypto"].encrypt(TeamLeaveOk_Message.id, TeamLeaveOk_Message.buffer)
		TeamLeaveOk_Message.pack()
		self.buffer += TeamLeaveOk_Message.buffer
