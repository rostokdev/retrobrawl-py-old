from packets.Messages import Message
from utils.reader import Reader
from utils.writer import Writer
import json
import collections 

class AllianceStreamEntryMessage(Message):
	def __init__(self, dictMessage, codeEntry):
		super().__init__()
		self.id = 24312
		self.dictMessage = dictMessage
		self.codeEntry = codeEntry

	def decode(self, buffer):
		Reader.__init__(self, buffer)

	def encode(self):
		Writer.__init__(self)
		# 3 - JoinRequestAllianceStreamEntry, 2 - ChatStreamEntry, 4 - AllianceEventStreamEntry, 5 - ReplayStreamEntry, default: TeamCreatedStreamEntry
		if (self.codeEntry == 2):
			#collections.deque(a, maxlen=1)

			self.writeVint(2)

			self.writeVint(0)
			self.writeVint(self.dictMessage["LowID"])

			self.writeVint(0)
			self.writeVint(self.dictMessage["fromLowID"])

			self.writeString(self.dictMessage["fromName"])

			self.writeVint(0)
			self.writeVint(0)

			self.writeBoolean(False)

			self.writeString(self.dictMessage["message"])

