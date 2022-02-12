from packets.Messages import Message
from utils.reader import Reader
from utils.writer import Writer


class TeamMessage(Message):
	def __init__(self, player):
		super().__init__()
		self.id = 24124
		self.player = player

	def decode(self, buffer):
		Reader.__init__(self, buffer)

	def encode(self):
		self.writeVint(1)

		self.writeBoolean(False)

		self.writeVint(0)

		self.writeInt32(0)
		self.writeInt32(1)

		self.writeVint(0)

		self.writeByte(0) # 2 bool

		self.writeVint(0)
		self.writeVint(0)

		self.writeScID(15, 0)

		self.writeVint(1)
		for x in range(1):
			self.writeBoolean(True)

			self.writeInt32(0)
			self.writeInt32(1)

			self.writeString(self.player.DataDB["name"])

			self.writeVint(0)

			self.writeScID(16, 0)
			self.writeScID(29, 0)

			self.writeVint(0)
			self.writeVint(0)
			self.writeVint(0)
			self.writeVint(0)

			self.writeBoolean(False)

			self.writeVint(0)

		self.writeVint(0)
		for x in range(0):
			self.writeInt32(0)
			self.writeInt32(1)

			self.writeString("ROSTIKDEV")

			self.writeVint(0)
			self.writeVint(0)