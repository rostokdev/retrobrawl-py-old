from packets.factories import MessageFactory
from packets.Messages.Client.ClientHelloMessage import ClientHelloMessage
from packets.Messages.Client.LoginMessage import LoginMessage
from packets.Messages.Client.ChangeAvatarNameMessage import ChangeAvatarNameMessage
from packets.Messages.Client.GetPlayerProfileMessage import GetPlayerProfileMessage
from packets.Messages.Client.TeamCreateMessage import TeamCreateMessage
from packets.Messages.Client.TeamSetMemberReadyMessage import TeamSetMemberReadyMessage
from packets.Messages.Client.KeepAliveMessage import KeepAliveMessage
from packets.Messages.Client.GetLeaderboardMessage import GetLeaderboardMessage
from packets.Messages.Client.UnlockAccountMessage import UnlockAccountMessage
from packets.Messages.Client.GoHomeFromOfflinePractiseMessage import GoHomeFromOfflinePractiseMessage
from packets.Messages.Client.TeamLeaveMessage import TeamLeaveMessage
from packets.Messages.Client.CreateAllianceMessage import CreateAllianceMessage
from packets.Messages.Client.AskForAllianceDataMessage import AskForAllianceDataMessage
from packets.Messages.Client.LeaveAllianceMessage import LeaveAllianceMessage
from packets.Messages.Client.JoinAllianceMessage import JoinAllianceMessage
from packets.Messages.Client.AskForJoinableAlliancesListMessage import AskForJoinableAlliancesListMessage
from packets.Messages.Client.ChatToAllianceStreamMessage import ChatToAllianceStreamMessage

message_factory = MessageFactory()
#command_factory = CommandFactory()

message_factory[10101] = LoginMessage
message_factory[10212] = ChangeAvatarNameMessage
message_factory[14600] = ChangeAvatarNameMessage
message_factory[14113] = GetPlayerProfileMessage
message_factory[10100] = ClientHelloMessage
message_factory[14350] = TeamCreateMessage
message_factory[14355] = TeamSetMemberReadyMessage
message_factory[10108] = KeepAliveMessage
message_factory[14403] = GetLeaderboardMessage
message_factory[10121] = UnlockAccountMessage
message_factory[14109] = GoHomeFromOfflinePractiseMessage
message_factory[14353] = TeamLeaveMessage
message_factory[14301] = CreateAllianceMessage
message_factory[14302] = AskForAllianceDataMessage
message_factory[14308] = LeaveAllianceMessage
message_factory[14305] = JoinAllianceMessage
message_factory[14303] = AskForJoinableAlliancesListMessage
message_factory[14315] = ChatToAllianceStreamMessage

#command_factory[14102] = None # EndClientTurnMessage

# message_factory[packet_id] = class_of_this_packet
