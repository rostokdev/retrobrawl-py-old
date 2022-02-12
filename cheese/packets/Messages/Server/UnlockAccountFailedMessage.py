from packets.Messages import Message
from utils.reader import Reader
from utils.writer import Writer


class UnlockAccountFailedMessage(Message):
	def __init__(self):
		super().__init__()
		self.id = 20133

	def decode(self, buffer):
		Reader.__init__(self, buffer)

	def encode(self):
		Writer.__init__(self)

		self.writeInt32(1)