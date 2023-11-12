import socket

ip = "172.16.13.56"
port = 1234

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
s.bind((ip,port))

data, addr= s.recvfrom(1024)
print(str(addr)+data.decode())

data = input("please enter data ")
s.sendto(data.encode(),addr)