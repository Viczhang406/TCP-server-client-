import socket

ip = "172.16.13.55"
port = 1234

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
while True:
    data = input("please enter data ")
    s.sendto(data.encode(),(ip,port))
    data, addr= s.recvfrom(1024)
    print(str(addr)+data.decode())





