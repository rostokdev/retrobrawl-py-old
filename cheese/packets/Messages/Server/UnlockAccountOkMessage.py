from packets.Messages import Message
from utils.reader import Reader
from utils.writer import Writer


class UnlockAccountOkMessage(Message):
	def __init__(self, player):
		super().__init__()
		self.id = 20132
		self.player = player

	def decode(self, buffer):
		Reader.__init__(self, buffer)

	def encode(self):
		Writer.__init__(self)

		self.writeInt32(0)
		self.writeInt32(self.player.DataDB["LowID"])

		self.writeString(self.player.DataDB["Token"])