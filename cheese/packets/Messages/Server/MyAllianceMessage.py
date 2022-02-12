from packets.Messages import Message
from utils.reader import Reader
from utils.writer import Writer


class MyAllianceMessage(Message):
	def __init__(self, dataClub, isClub=True):
		super().__init__()
		self.id = 24399
		self.dataClub = dataClub
		self.isClub = isClub

	def decode(self, buffer):
		Reader.__init__(self, buffer)

	def encode(self):
		Writer.__init__(self)
		if self.isClub:
			self.writeVint(0)
			self.writeBoolean(True)

			self.writeScID(25, 0)

			self.writeInt32(0)
			self.writeInt32(self.dataClub["LowID"])

			self.writeString(self.dataClub["name"])

			self.writeScID(8, 0)

			self.writeVint(0)
			self.writeVint(0)
			self.writeVint(0)
			self.writeVint(0)

			self.writeScID(0, 0)

			self.writeVint(3)
		else:
			self.writeVint(0)
			self.writeVint(0)
