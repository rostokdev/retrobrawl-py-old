from packets.Messages import Message
from utils.reader import Reader
from utils.writer import Writer


class PlayerProfileMessage(Message):
	def __init__(self, dataDB):
		super().__init__()
		self.id = 24113
		self.dataDB = dataDB

	def decode(self, buffer):
		Reader.__init__(self, buffer)

	def encode(self):
		Writer.__init__(self)
		self.writeVint(0)
		self.writeVint(self.dataDB["LowID"])

		self.writeString(self.dataDB["name"])  # Name 
		self.writeScID(28, 0)

		self.writeVint(0)
		for x in range(0):
			pass

		self.writeVint(14)
		for x in range(14):
			self.writeVint(x+1)
			self.writeVint(100000)
