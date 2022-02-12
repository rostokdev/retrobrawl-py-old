from packets.Messages import Message
from utils.reader import Reader
from utils.writer import Writer


class LoginOk(Message):
    def __init__(self, player):
        super().__init__()
        self.id = 20104
        self.player = player
        print(self.player.Token)

    def decode(self, buffer):
        Reader.__init__(self, buffer)

    def encode(self):
        Writer.__init__(self)
        self.writeInt32(0)
        self.writeInt32(self.player.LowID)
        
        self.writeInt32(0)
        self.writeInt32(self.player.LowID)
        
        self.writeString(self.player.Token)
        
        self.writeString()
        self.writeString()
        
        self.writeVint(12)
        self.writeVint(0)
        self.writeVint(186)
        
        self.writeString()
        self.writeString()
        self.writeString()
        
        self.writeVint(0)
        self.writeString("G:1")
        self.writeString()
        
        self.writeString("UA")
        self.writeString("Kiev")
        
        self.writeString()
        self.writeString()
        self.writeString()
