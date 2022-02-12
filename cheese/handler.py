from packets.message_factory import message_factory
from utils.console import Console
from utils.reader import Reader
from utils.CryptoBs import *
from logic.Player import Player
from logic.Device import Device

class Handler(Reader):
    def __init__(self, client, address, clientsAll):
        super().__init__(b'')
        self.client = client
        self.address = address
        self.player = Player()
        self.device = Device()
        self.player.clientsAll = clientsAll
        self.player.device = self.device
        self.player.crypto = CryptoBs("03BBE171010D8F928E7B3B71773CCBEF75AE4B02E6D7B11BC760ED3AE853C839", self.player.device)
        self.player.address = address
        self.player.client = client
       # self.player.client = self.client

        self.console = Console('PyBrawl')
        self.client_console = Console('Client')

        self.handle()

    def handle(self):
        while True:
            try:
                data = self.client.recv(7)
                if data:
                    super().__init__(data)

                    packet_id = self.readUShort()
                    packet_length = self.readUInt(3)
                    packet_version = self.readUShort()

                    packet_data = self.receive(packet_length)

                    self.client_console.update_prefix(f'Client - {packet_id}')
                    self.client_console.print(f'Length: {packet_length}')

                    message = message_factory[packet_id]
                    #print(self.player.device.state)
                    packet_data = self.player.crypto.decrypt(packet_id, packet_data)
                    if message:
                        message = message(self.player)
                        message.decode(packet_data)
                        isSend = message.process()
                        if isSend == None:
                            self.client.send(message.buffer)
            except ConnectionResetError:
                if (len(self.DataDB["alliance"]) > 0):
                    self.player.clientsAll["clubs"][str(self.DataDB["alliance"]["LowID"])].pop(str(self.DataDB["LowID"]))
                self.console.print(f'{self.address[0]}:{self.address[1]} is disconnected!')
                break

    def receive(self, packet_length):
        data = b''
        while len(data) < packet_length:
            data += self.client.recv(packet_length)
        return data
