from packets.Messages import Message
from utils.reader import Reader
from utils.writer import Writer


class TeamLeftMessage(Message):
	def __init__(self, player):
		super().__init__()
		self.id = 24125
		self.player = player
		print(self.player.Token)

	def decode(self, buffer):
		Reader.__init__(self, buffer)

	def encode(self):
		Writer.__init__(self)
		self.writeInt32(0)