import socket
import os

socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
ip = "127.0.0.1"
port = 9800
addr = ip,port

filename = input("input your file name : ")
f=open(filename,"rb")
data=f.read(1024)

socket.sendto(str(os.path.getsize(filename)).encode(),addr)
data_transferred = 0
while data:
    print(data)
    data_transferred += len(data)
    socket.sendto(data,addr)
    print('current / totalsize = ',data_transferred,'/',int(str(os.path.getsize(filename)).encode()),',',(data_transferred/int(str(os.path.getsize(filename)).encode())*100)
            )
    data = f.read(1024)


f.close()
print("ok")
socket.close()
print("file_send_end")

