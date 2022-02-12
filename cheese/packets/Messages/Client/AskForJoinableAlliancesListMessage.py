from packets.Messages import Message
from packets.Messages.Server.JoinableAllianceListMessage import JoinableAllianceListMessage

class AskForJoinableAlliancesListMessage(Message):
    def __init__(self, player):
        super().__init__()
        self.id = 14303
        self.player = player

    def decode(self, buffer):
        super().decode(buffer)

    def process(self):
        dataClubs = self.player.dbClub.get_search_club_db()
        JoinableAllianceList_Message = JoinableAllianceListMessage(dataClubs)
        JoinableAllianceList_Message.encode()
        JoinableAllianceList_Message.buffer = self.player.clientsAll["players"][str(self.player.LowID)]["crypto"].encrypt(JoinableAllianceList_Message.id, JoinableAllianceList_Message.buffer)
        JoinableAllianceList_Message.pack()
        self.buffer = JoinableAllianceList_Message.buffer

