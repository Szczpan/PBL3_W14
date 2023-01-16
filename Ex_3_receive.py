import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
sock.bind(("192.168.114.193", 21054))
count = 0
sock.listen(1)
sock.accept()
while True:
    data, address = sock.recv(65507)
    print(data.decode('utf-8'))
    if address == "192.168.114.122":
        count += 1
