import threading
import socket
from logic.Player import Player
from logic.Device import Device
from handler import Handler


class Server:
    def __init__(self):
        self.socket = socket.socket()

    def start(self, ip="0.0.0.0", port=None):
        if ip is None:
            ip = 'localhost'
        if port is None:
            port = 9339

        self.clientsAll = {}
        self.clientsAll["clubs"] = {}
        self.clientsAll["players"] = {}

        self.socket.bind((ip, port))
        print(f"[INFO] Server starting! IP: {ip}, PORT: {port}")

    def listen(self):
        self.socket.listen()
        while True:
            client, address = self.socket.accept()
            #player = Player()
           # device = Device()

            print(f'[INFO] Connect from {address[0]}:{address[1]}')

            client_thread = threading.Thread(target=Handler, args=(client, address, self.clientsAll))
            client_thread.start()


if __name__ == '__main__':
    server = Server()
    server.start()
    server.listen()
