from packets.Messages import Message
from packets.Messages.Server.LeaderboardMessage import LeaderboardMessage

class GetLeaderboardMessage(Message):
    def __init__(self, player):
        super().__init__()
        self.id = 14403
        self.player = player

    def decode(self, buffer):
        super().decode(buffer)

    def process(self):
        dataDB = self.player.db.get_top_players_db()
        Leaderboard_Message = LeaderboardMessage(dataDB)
        Leaderboard_Message.encode()
        Leaderboard_Message.buffer = self.player.clientsAll["players"][str(self.player.LowID)]["crypto"].encrypt(Leaderboard_Message.id, Leaderboard_Message.buffer)
        Leaderboard_Message.pack()
        self.buffer = Leaderboard_Message.buffer
        """
        self.buffer = login_ok.buffer
        self.buffer += ohd.buffer
        """
