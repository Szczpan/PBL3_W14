import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
sock.bind(("192.168.114.193", 12054))
count = 0
# sock.listen(1)
# sock.accept()
while True:
    data, address = sock.recvfrom(65000)
    print(data.decode('utf-8'))
    if address == "192.168.114.122":
        count += 1
        print(count)
