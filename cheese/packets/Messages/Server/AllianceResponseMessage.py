from packets.Messages import Message
from utils.reader import Reader
from utils.writer import Writer


class AllianceResponseMessage(Message):
	def __init__(self, code):
		super().__init__()
		self.id = 24333
		self.code = code

	def decode(self, buffer):
		Reader.__init__(self, buffer)

	def encode(self):
		Writer.__init__(self)
		self.writeVint(self.code)