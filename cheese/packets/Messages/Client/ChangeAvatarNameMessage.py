from packets.Messages import Message
from packets.Commands.Server.Change_Name_Callback import Change_Name_Callback

class ChangeAvatarNameMessage(Message):
    def __init__(self, player):
        super().__init__()
        self.id = 10212
        self.player = player

    def decode(self, buffer):
        super().decode(buffer)
        name = self.readString()

        self.player.set_name(name)

    def process(self):
        change_name = Change_Name_Callback(self.player)
        change_name.encode()
        change_name.buffer = self.player.clientsAll["players"][str(self.player.LowID)]["crypto"].encrypt(change_name.id, change_name.buffer)
        change_name.pack()
        self.buffer = change_name.buffer 
        """
        self.buffer = login_ok.buffer
        self.buffer += ohd.buffer
        """
