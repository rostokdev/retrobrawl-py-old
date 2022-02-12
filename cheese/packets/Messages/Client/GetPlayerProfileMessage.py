from packets.Messages import Message
from packets.Messages.Server.PlayerProfileMessage import PlayerProfileMessage

class GetPlayerProfileMessage(Message):
    def __init__(self, player):
        super().__init__()
        self.id = 14113
        self.player = player

    def decode(self, buffer):
        super().decode(buffer)
        highID = self.readUInt32()
        self.lowID = self.readUInt32()
        #unk = self.readBool()


    def process(self):
        dataDB = self.player.get_data_by_lowID(self.lowID)
        vis_home_data = PlayerProfileMessage(dataDB)
        vis_home_data.encode()
        vis_home_data.buffer = self.player.clientsAll["players"][str(self.player.LowID)]["crypto"].encrypt(vis_home_data.id, vis_home_data.buffer)
        vis_home_data.pack()
        self.buffer = vis_home_data.buffer
        """
        self.buffer = login_ok.buffer
        self.buffer += ohd.buffer
        """
