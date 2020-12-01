#!/usr/bin/env python

import socket

TCP_IP = '127.0.0.1'
TCP_PORT = 12345
BUFFER_SIZE = 20


class TCP:

    def __init__(self, solution: []):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect((TCP_IP, TCP_PORT))

        self.solution = solution
        self._cmd()

    def _cmd(self):
        x = 0
        y = 0
        for val in self.solution:
            tx = val[0]
            ty = val[1]

            if tx > x:  # RIGHT
                b = bytes("[0][255][255][0]", 'utf-8')
                self.s.send(b)
            elif tx < x:  # LEFT
                b = bytes("[255][0][0][255]", 'utf-8')
                self.s.send(b)
                b = bytes("[0][255][0][255]", 'utf-8')
                self.s.send(b)
            elif ty < y:  # UP
                b = bytes("[255][0][255][0]", 'utf-8')
                self.s.send(b)

            x = tx
            y = ty
        b = bytes("[0][0][0][0]", 'utf-8')
        self.s.send(b)
        data = self.s.recv(BUFFER_SIZE)
        self.s.close()
        print(data)
