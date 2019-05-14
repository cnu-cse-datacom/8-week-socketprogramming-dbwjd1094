import socket
FLAGS = None

socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
ip = "192.168.31.139"
port = 9100
addr(ip,port)

filename = input("input your file name : ")
f=open(filename,"rb")
data=f.read(1024)

socket.sendto(str(os.path.getsize(filename)).encode(),addr)
while data:
    data_transferred += len(data)
    data=f.read(1024)
    socket.sendto(data,addr)
    print('current / totalsize = ',data_transferred,'/',int(str(os.path.getsize(filename)).encode()),',',(data_transferred/int(str(os.path.getsize(filename)).encode())*100)

print("ok")
f.close()
socket.close()
print("file_send_end")

