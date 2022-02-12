from packets.Messages import Message
from packets.Messages.Server.MyAllianceMessage import MyAllianceMessage
from packets.Messages.Server.AllianceResponseMessage import AllianceResponseMessage

class LeaveAllianceMessage(Message):
    def __init__(self, player):
        super().__init__()
        self.id = 14308
        self.player = player

    def decode(self, buffer):
        super().decode(buffer)

    def process(self):
        lowID = self.player.DataDB["alliance"]["LowID"]
        self.player.removePlayerFromAlliance()
        self.player.DataDB["alliance"] = {}
        self.player.setData()

        AllianceResponse_Message = AllianceResponseMessage(80)
        AllianceResponse_Message.encode()
        AllianceResponse_Message.buffer = self.player.clientsAll["players"][str(self.player.LowID)]["crypto"].encrypt(AllianceResponse_Message.id, AllianceResponse_Message.buffer)
        AllianceResponse_Message.pack()
        self.buffer = AllianceResponse_Message.buffer

        MyAlliance_Message = MyAllianceMessage(None, False)
        MyAlliance_Message.encode()
        MyAlliance_Message.buffer = self.player.clientsAll["players"][str(self.player.LowID)]["crypto"].encrypt(MyAlliance_Message.id, MyAlliance_Message.buffer)
        MyAlliance_Message.pack()
        self.buffer += MyAlliance_Message.buffer

        self.player.clientsAll["clubs"][str(lowID)].remove(str(self.player.DataDB["LowID"]))

