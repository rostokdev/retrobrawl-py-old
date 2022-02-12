from packets.Messages import Message
from utils.reader import Reader
from utils.writer import Writer
import json
import collections 

class AllianceStreamMessage(Message):
	def __init__(self, dictMessages):
		super().__init__()
		self.id = 24311
		self.dictMessages = dictMessages

	def decode(self, buffer):
		Reader.__init__(self, buffer)

	def encode(self):
		Writer.__init__(self)
		# 3 - JoinRequestAllianceStreamEntry, 2 - ChatStreamEntry, 4 - AllianceEventStreamEntry, 5 - ReplayStreamEntry, default: TeamCreatedStreamEntry
		self.writeVint(len(self.dictMessages))

		for x in self.dictMessages:
			x = self.dictMessages[x]
			self.writeVint(2)

			self.writeVint(0)
			self.writeVint(x["LowID"])

			self.writeVint(0)
			self.writeVint(x["fromLowID"])

			self.writeString(x["fromName"])

			self.writeVint(0)
			self.writeVint(0)

			self.writeBoolean(False)

			self.writeString(x["message"])

