from packets.Messages import Message
from utils.reader import Reader
from utils.writer import Writer


class KeepAliveOkMessage(Message):
	def __init__(self, player):
		super().__init__()
		self.id = 20108
		self.player = player

	def decode(self, buffer):
		Reader.__init__(self, buffer)

	def encode(self):
		pass