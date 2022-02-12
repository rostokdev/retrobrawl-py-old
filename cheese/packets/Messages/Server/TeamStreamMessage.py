from packets.Messages import Message
from utils.reader import Reader
from utils.writer import Writer


class TeamStreamMessage(Message):
	def __init__(self, player):
		super().__init__()
		self.id = 24131
		self.player = player

	def decode(self, buffer):
		Reader.__init__(self, buffer)

	def encode(self):
		self.writeVint(0)
		self.writeVint(0)

		self.writeVint(-1)