import socket

ip = "172.20.176.1"  #當前設備IP
port = 1122

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
data = (ip,port)
s.connect((ip,port))

while True:
    enterdata = input("please insert data ")
    s.send(enterdata.encode())
    Getdata = s.recv(1024)
    print(Getdata.decode())
    if enterdata == "close":
        s.close()
