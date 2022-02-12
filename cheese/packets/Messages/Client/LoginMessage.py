from packets.Messages import Message
from packets.Messages.Server.LoginOkMessage import LoginOk
from packets.Messages.Server.OwnHomeDataMessage import OwnHomeData
from packets.Messages.Server.LoginFailedMessage import LoginFailedMessage
from packets.Messages.Server.MyAllianceMessage import MyAllianceMessage
import json
from packets.Messages.Server.AllianceStreamMessage import AllianceStreamMessage

class LoginMessage(Message):
    def __init__(self, player):
        super().__init__()
        self.id = 10101
        self.player = player

    def decode(self, buffer):
        super().decode(buffer)
        highID = self.readUInt32()
        lowID = self.readUInt32()
        token = self.readString()  # Pass Token
        """
        major = self.readUInt32()
        revision = self.readUInt32()
        build = self.readUInt32()
        master_hash = self.readString()
        phone_model = self.readString()
        locale_key = self.readShort()
        language = self.readString()
        os_version = self.readString()
        is_android = self.readBool()
        self.readString()
        android_device_id = self.readString()
        
        self.readBool()  # isAdvertisingTrackingEnabled
        self.readString()  # vendor_uuid
        self.readUInt32()
        self.readUByte()
        version = self.readString()

        [self.readByte() for x in range(49)]  # idk what is it

        if self.readBool():  # Ultra info
            self.readString()
        """

        self.player.Token = token
        self.player.HighID = highID
        self.player.LowID = lowID
        self.player.get_info()

    def process(self):
        self.player.device.state = self.player.device.StateLogin
        """
        LoginFailed_Message = LoginFailedMessage(self.player, 10)
        LoginFailed_Message.encode()
        LoginFailed_Message.buffer = self.player.crypto.encrypt(LoginFailed_Message.id, LoginFailed_Message.buffer)
        LoginFailed_Message.pack()
        self.player.device.state = self.player.device.StateLogged 
        self.buffer = LoginFailed_Message.buffer
        """
        
        if self.player.DataDB["access"] == False:
            self.player.clientsAll["players"][str(self.player.LowID)] = {}
            self.player.clientsAll["players"][str(self.player.LowID)]["client"], self.player.clientsAll["players"][str(self.player.LowID)]["crypto"] =  self.player.client, self.player.crypto

            login_ok = LoginOk(self.player)
            login_ok.encode()
            login_ok.buffer = self.player.clientsAll["players"][str(self.player.LowID)]["crypto"].encrypt(login_ok.id, login_ok.buffer)
            login_ok.pack()
            self.buffer = login_ok.buffer
            self.player.device.state = self.player.device.StateLogged

            ohd = OwnHomeData(self.player)
            ohd.encode()
            ohd.buffer = self.player.clientsAll["players"][str(self.player.LowID)]["crypto"].encrypt(ohd.id, ohd.buffer)
            ohd.pack()
            self.buffer += ohd.buffer
            if (len(self.player.DataDB["alliance"]) > 0):
                if str(self.player.DataDB["alliance"]["LowID"]) not in self.player.clientsAll["clubs"]:
                    self.player.clientsAll["clubs"][str(self.player.DataDB["alliance"]["LowID"])] = []

                self.player.clientsAll["clubs"][str(self.player.DataDB["alliance"]["LowID"])].append(str(self.player.LowID))

                dataClub = json.loads(self.player.getAliiance_lowId(self.player.DataDB["alliance"]["LowID"])[0][1])

                MyAlliance_Message = MyAllianceMessage(dataClub)
                MyAlliance_Message.encode()
                MyAlliance_Message.buffer = self.player.clientsAll["players"][str(self.player.LowID)]["crypto"].encrypt(MyAlliance_Message.id, MyAlliance_Message.buffer)
                MyAlliance_Message.pack()
                self.buffer += MyAlliance_Message.buffer

                AllianceStream_Message = AllianceStreamMessage(dataClub["messages"])
                AllianceStream_Message.encode()
                AllianceStream_Message.buffer = self.player.clientsAll["players"][str(self.player.LowID)]["crypto"].encrypt(AllianceStream_Message.id, AllianceStream_Message.buffer)
                AllianceStream_Message.pack()
                self.buffer += AllianceStream_Message.buffer
        else:
            LoginFailed_Message = LoginFailedMessage(self.player, 13)
            LoginFailed_Message.encode()
            LoginFailed_Message.encrypt()
            #LoginFailed_Message.buffer = self.player.crypto.encrypt(LoginFailed_Message.id, LoginFailed_Message.buffer)
            LoginFailed_Message.pack()
            self.buffer = LoginFailed_Message.buffer
            self.player.device.state = self.player.device.StateLogged 
        #return False
