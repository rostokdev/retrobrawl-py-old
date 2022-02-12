from packets.Messages import Message
from packets.Messages.Server.MyAllianceMessage import MyAllianceMessage
from packets.Messages.Server.AllianceResponseMessage import AllianceResponseMessage
from packets.Messages.Server.AllianceStreamMessage import AllianceStreamMessage

class JoinAllianceMessage(Message):
    def __init__(self, player):
        super().__init__()
        self.id = 14305
        self.player = player

    def decode(self, buffer):
        super().decode(buffer)
        self.readInt32()
        self.lowid = self.readInt32()

    def process(self):
        self.player.DataDB["alliance"] = {"LowID": self.lowid}
        self.player.setData()
        dataClub = self.player.addPlayerToAlliance()

        AllianceResponse_Message = AllianceResponseMessage(40)
        AllianceResponse_Message.encode()
        AllianceResponse_Message.buffer = self.player.clientsAll["players"][str(self.player.LowID)]["crypto"].encrypt(AllianceResponse_Message.id, AllianceResponse_Message.buffer)
        AllianceResponse_Message.pack()
        self.buffer = AllianceResponse_Message.buffer

        MyAlliance_Message = MyAllianceMessage(dataClub)
        MyAlliance_Message.encode()
        MyAlliance_Message.buffer = self.player.clientsAll["players"][str(self.player.LowID)]["crypto"].encrypt(MyAlliance_Message.id, MyAlliance_Message.buffer)
        MyAlliance_Message.pack()

        AllianceStream_Message = AllianceStreamMessage(dataClub["messages"])
        AllianceStream_Message.encode()
        AllianceStream_Message.buffer = self.player.clientsAll["players"][str(self.player.LowID)]["crypto"].encrypt(AllianceStream_Message.id, AllianceStream_Message.buffer)
        AllianceStream_Message.pack()

        self.buffer += MyAlliance_Message.buffer
        self.buffer += AllianceStream_Message.buffer

        if (str(self.player.DataDB["alliance"]["LowID"]) not in self.player.clientsAll["clubs"]):
            self.player.clientsAll["clubs"][str(self.player.DataDB["alliance"]["LowID"])] = []

        self.player.clientsAll["clubs"][str(self.player.DataDB["alliance"]["LowID"])].append(str(self.player.LowID))
        #self.player.clientsAll["clubs"][str(self.player.DataDB["alliance"]["LowID"])][str(self.player.DataDB["LowID"])]["client"] = self.player.client
        #self.player.clientsAll["clubs"][str(self.player.DataDB["alliance"]["LowID"])][str(self.player.DataDB["LowID"])]["crypto"] = self.player.crypto


