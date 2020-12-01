#!/usr/bin/python

import socket  # Import socket module

HOST = '0.0.0.0'
PORT = 12345


class Server:

    def __init__(self):
        self.s = socket.socket()
        self.s.bind((HOST, PORT))
        self.s.listen(5)
