from packets.Messages import Message
from utils.reader import Reader
from utils.writer import Writer


class ServerHelloMessage(Message):
    def __init__(self, player):
        super().__init__()
        self.id = 20100
        self.player = player

    def decode(self, buffer):
        Reader.__init__(self, buffer)

    def encode(self):
        Writer.__init__(self)
        self.buffer += b'\x00\x00\x00\x18\x13Y\xd8\x13M\x19\xf6\xffv\xe7q{\xb0\x9dl\x0c\x81\xe7)(\x9b\t\xc3\xfc'