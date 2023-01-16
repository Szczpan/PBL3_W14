import socket
import string
import random

UDP_IP = "192.168.114.255"
UDP_PORT = 12055
MESSAGE = ""

for i in range(65507):
    MESSAGE += random.choice(string.ascii_letters)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
while True:
    sock.sendto(bytes(MESSAGE, "utf-8"), (UDP_IP, UDP_PORT))
    # print(MESSAGE)