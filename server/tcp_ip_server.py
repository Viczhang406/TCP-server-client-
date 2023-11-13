import socket

ip = "172.20.176.1"
port = 1122
max_connect = 2


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
s.bind((ip,port))
s.listen(max_connect)

connect , address = s.accept()
print(address)

while True:
    data = connect.recv(1024)
    dataString = data.decode()
    print(dataString)
    echo_data = input("please insert anything ")
    connect.send(echo_data.encode())
    if dataString == "close":
        connect.close()
