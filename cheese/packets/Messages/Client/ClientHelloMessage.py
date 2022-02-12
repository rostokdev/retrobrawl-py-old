from packets.Messages import Message
from packets.Messages.Server.ServerHelloMessage import ServerHelloMessage

class ClientHelloMessage(Message):
    def __init__(self, player):
        super().__init__()
        self.id = 10100
        self.player = player

    def decode(self, buffer):
        pass

    def process(self):
        ServerHello_Message = ServerHelloMessage(self.player)
        ServerHello_Message.encode()
        ServerHello_Message.encode()
        ServerHello_Message.buffer = self.player.crypto.encrypt(ServerHello_Message.id, ServerHello_Message.buffer)
        ServerHello_Message.pack()
        self.player.device.state = self.player.device.StateLogin

        self.buffer = ServerHello_Message.buffer
