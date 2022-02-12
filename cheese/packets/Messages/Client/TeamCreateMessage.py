from packets.Messages import Message
from packets.Messages.Server.TeamMessage import TeamMessage
from packets.Messages.Server.TeamStreamMessage import TeamStreamMessage


class TeamCreateMessage(Message):
	def __init__(self, player):
		super().__init__()
		self.id = 14350
		self.player = player

	def decode(self, buffer):
		super().decode(buffer)

	def process(self):
		TeamStream_Message = TeamStreamMessage(self.player)
		TeamStream_Message.encode()
		TeamStream_Message.buffer = self.player.clientsAll["players"][str(self.player.LowID)]["crypto"].encrypt(TeamStream_Message.id, TeamStream_Message.buffer)
		TeamStream_Message.pack()
		
		Team_Message = TeamMessage(self.player)
		Team_Message.encode()
		Team_Message.buffer = self.player.clientsAll["players"][str(self.player.LowID)]["crypto"].encrypt(Team_Message.id, Team_Message.buffer)
		Team_Message.pack()
		
		self.buffer = TeamStream_Message.buffer
		self.buffer += Team_Message.buffer
