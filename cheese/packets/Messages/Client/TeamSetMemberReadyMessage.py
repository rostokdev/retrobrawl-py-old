from packets.Messages import Message
from packets.Messages.Server.TeamGameStartingMessage import TeamGameStartingMessage


class TeamSetMemberReadyMessage(Message):
	def __init__(self, player):
		super().__init__()
		self.id = 14355
		self.player = player

	def decode(self, buffer):
		super().decode(buffer)

	def process(self):
		TeamGameStarting_Message = TeamGameStartingMessage(self.player)
		TeamGameStarting_Message.encode()
		TeamGameStarting_Message.buffer = self.player.clientsAll["players"][str(self.player.LowID)]["crypto"].encrypt(TeamGameStarting_Message.id, TeamGameStarting_Message.buffer)
		TeamGameStarting_Message.pack()
		
		self.buffer = TeamGameStarting_Message.buffer

