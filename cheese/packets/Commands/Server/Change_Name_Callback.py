from packets.Messages import Message
from utils.reader import Reader
from utils.writer import Writer


class Change_Name_Callback(Message):
    def __init__(self, player):
        super().__init__()
        self.id = 24111
        self.commandID = 201
        self.player = player

    def decode(self, buffer):
        Reader.__init__(self, buffer)

    def encode(self):
        Writer.__init__(self)
        self.writeVint(self.commandID)

        self.writeString(self.player.DataDB["name"])
        self.writeVint(0)
