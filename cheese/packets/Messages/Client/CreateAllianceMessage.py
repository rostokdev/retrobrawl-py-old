from packets.Messages import Message
from packets.Messages.Server.MyAllianceMessage import MyAllianceMessage
from packets.Messages.Server.AllianceResponseMessage import AllianceResponseMessage

class CreateAllianceMessage(Message):
    def __init__(self, player):
        super().__init__()
        self.id = 14301
        self.player = player

    def decode(self, buffer):
        super().decode(buffer)
        self.nameClub = self.readString()
        self.description = self.readString()

        self.readScID() # icon 

        self.readVint()
        self.readVint()

    def process(self):
        lowid = self.player.dbClub.low_id_desc_db()
        lowid_player = self.player.DataDB["LowID"]
        dataClub = {"name": self.nameClub, "description": self.description, "trophies": 5000, 
        "LowID": self.player.dbClub.low_id_desc_db(), "players": {f"{lowid_player}": {"name": self.player.DataDB["name"], 
        "role": "2", "trophies": self.player.DataDB["trophies"], "LowID": lowid_player}}, 
        "messages": {}}
        self.player.DataDB["alliance"] = {"LowID": lowid}

        self.player.setData()
        self.player.createAlliance(dataClub)

        MyAlliance_Message = MyAllianceMessage(dataClub)
        MyAlliance_Message.encode()
        MyAlliance_Message.buffer = self.player.clientsAll["players"][str(self.player.LowID)]["crypto"].encrypt(MyAlliance_Message.id, MyAlliance_Message.buffer)
        MyAlliance_Message.pack()
        self.buffer = MyAlliance_Message.buffer
        if (str(self.player.DataDB["alliance"]["LowID"]) not in self.player.clientsAll["clubs"]):
            self.player.clientsAll["clubs"][str(self.player.DataDB["alliance"]["LowID"])] = []

        self.player.clientsAll["clubs"][str(self.player.DataDB["alliance"]["LowID"])].append(str(self.player.LowID))
        #self.player.clientsAll["players"][str(self.player.LowID)] = {}
        #self.player.clientsAll["players"][str(self.player.LowID)] = {}
        #self.player.clientsAll["players"][str(self.player.LowID)]["client"], self.player.clientsAll["players"][str(self.player.LowID)]["crypto"] =  self.player.client, self.player.crypto
        """
        AllianceResponse_Message = AllianceResponseMessage(dataClub)
        AllianceResponse_Message.encode()
        AllianceResponse_Message.buffer = self.player.crypto.encrypt(AllianceResponse_Message.id, AllianceResponse_Message.buffer)
        AllianceResponse_Message.pack()
        self.buffer += AllianceResponse_Message.buffer
        """