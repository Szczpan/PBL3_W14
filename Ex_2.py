import socket
import string
import random
from time import sleep
UDP_IP = "192.168.114.193"
UDP_PORT = 12054
MESSAGE = ""

for i in range(65507):
    MESSAGE += random.choice(string.ascii_letters)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
sock.connect((UDP_IP, UDP_PORT))
while True:
    packet_n = input("Podaj liczbę pakietów: ")
    packet_interval = input("Podaj okres nadawania w milisekundach: ")

    for i in range(int(packet_n)):
        sleep(int(packet_interval)/1000)
        sock.send(bytes(MESSAGE, "utf-8"))
