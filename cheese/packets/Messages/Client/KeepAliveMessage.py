from packets.Messages import Message
from packets.Messages.Server.KeepAliveOkMessage import KeepAliveOkMessage


class KeepAliveMessage(Message):
    def __init__(self, player):
        super().__init__()
        self.id = 10108
        self.player = player

    def decode(self, buffer):
        super().decode(buffer)

    def process(self):
        KeepAliveOk_Message = KeepAliveOkMessage(self.player)
        KeepAliveOk_Message.encode()
        KeepAliveOk_Message.pack()
        self.buffer += KeepAliveOk_Message.buffer