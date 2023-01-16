import socket
import string
import random
from time import sleep
UDP_IP = "192.168.114.193"
UDP_PORT = 12054
MESSAGE = ""

for i in range(65507):
    MESSAGE += random.choice(string.ascii_letters)

while True:
    packet_n = input("Podaj liczbę pakietów: ")
    packet_interval = input("Podaj okres nadawania w milisekundach: ")
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP

    for i in range(int(packet_n)):
        sleep(int(packet_interval)/1000)
        sock.sendto(bytes(MESSAGE, "utf-8"), (UDP_IP, UDP_PORT))
