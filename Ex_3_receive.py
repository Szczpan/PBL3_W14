import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
sock.bind(("192.168.114.193", 21054))
count = 0
while True:
    bufsiz, address = sock.recvfrom(65507)
    if bufsiz == 65507 and address == "192.168.114.122":
        count += 1
