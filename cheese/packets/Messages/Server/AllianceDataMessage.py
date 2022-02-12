from packets.Messages import Message
from utils.reader import Reader
from utils.writer import Writer


class AllianceDataMessage(Message):
	def __init__(self, dataClub):
		super().__init__()
		self.id = 24301
		self.dataClub = dataClub

	def decode(self, buffer):
		Reader.__init__(self, buffer)

	def encode(self):
		Writer.__init__(self)

		self.writeInt32(0)
		self.writeInt32(self.dataClub["LowID"])

		self.writeString(self.dataClub["name"])

		self.writeScID(8, 0)

		self.writeVint(1)
		self.writeVint(len(self.dataClub["players"]))

		self.writeVint(self.dataClub["trophies"])
		self.writeVint(0)

		self.writeScID(0, 0)
		self.writeVint(0)

		self.writeString("RU") # Location
		self.writeVint(len(self.dataClub["players"]))
		for x in self.dataClub['players']:
			x = self.dataClub['players'][x]
			self.writeInt32(0)
			self.writeInt32(x["LowID"])

			self.writeString(x["name"])

			self.writeVint(0)
			self.writeVint(0)
			self.writeVint(0)
			self.writeVint(0)
			self.writeVint(0)

			self.writeScID(28, 0)


