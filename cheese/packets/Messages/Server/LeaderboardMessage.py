from packets.Messages import Message
from utils.reader import Reader
from utils.writer import Writer
import json

class LeaderboardMessage(Message):
	def __init__(self, dataPlayers):
		super().__init__()
		self.id = 24403
		self.dataPlayers = dataPlayers

	def decode(self, buffer):
		Reader.__init__(self, buffer)

	def encode(self):
		self.writeVint(0)
		self.writeScID(0,0)
		self.writeString()

		self.writeVint(0)
		#for x in self.dataPlayers:
		#	d = json.loads(x[1])

		self.writeVint(-64)
		self.writeVint(-64)
		
		self.writeVint(1)
		self.writeVint(0)
		self.writeString("RU") # country

