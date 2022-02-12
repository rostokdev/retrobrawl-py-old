from packets.Messages import Message
from utils.reader import Reader
from utils.writer import Writer
import json

class JoinableAllianceListMessage(Message):
	def __init__(self, dataClubs):
		super().__init__()
		self.id = 24304
		self.dataClubs = dataClubs

	def decode(self, buffer):
		Reader.__init__(self, buffer)

	def encode(self):
		Writer.__init__(self)
		self.writeVint(len(self.dataClubs))
		for x in self.dataClubs:
			#print(self.dataClubs)
			x = json.loads(x[1])
			self.writeInt32(0)
			self.writeInt32(x["LowID"])

			self.writeString(x["name"])

			self.writeScID(8, 0)

			self.writeVint(0)
			self.writeVint(0)
			self.writeVint(0)
			self.writeVint(0)

			self.writeScID(0, 0)

			self.writeVint(3)

