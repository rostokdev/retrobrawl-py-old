from packets.Messages import Message
from packets.Messages.Server.AllianceStreamEntryMessage import AllianceStreamEntryMessage
import json
import threading
import collections

class ChatToAllianceStreamMessage(Message):
    def __init__(self, player):
        super().__init__()
        self.id = 14315
        self.player = player

    def senderAll(self):
        AllianceStreamEntry_Message = AllianceStreamEntryMessage(self.dictMessage, 2)
        AllianceStreamEntry_Message.encode()
        bufferP = AllianceStreamEntry_Message.buffer

        for x in self.player.clientsAll["clubs"][str(self.player.DataDB["alliance"]["LowID"])]:
            AllianceStreamEntry_Message.buffer = self.player.clientsAll["players"][x]["crypto"].encrypt(24312, bufferP)
            AllianceStreamEntry_Message.pack()
            self.player.clientsAll["players"][x]["client"].send(AllianceStreamEntry_Message.buffer)

    def decode(self, buffer):
        super().decode(buffer)
        self.message = self.readString()

    def process(self):
        dataClubs = json.loads(self.player.getAliiance_lowId(self.player.DataDB["alliance"]["LowID"])[0][1])
        try:
            [lastLowID] = collections.deque(dataClubs["messages"], maxlen=1)
            lastLowID = str(int(lastLowID) + 1)
        except:
            lastLowID = 0

        self.dictMessage = {"LowID": int(lastLowID), "message": self.message, "fromLowID": self.player.DataDB["LowID"], "fromName": self.player.DataDB["name"]}
        dataClubs["messages"][str(int(lastLowID))] = self.dictMessage
        self.player.dbClub.update_data_db(dataClubs, dataClubs["LowID"])

        client_thread = threading.Thread(target=self.senderAll)
        client_thread.start()
        #self.buffer = AllianceStreamEntry_Message.buffer

        return False

