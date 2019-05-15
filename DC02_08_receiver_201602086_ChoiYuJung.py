import socket

socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
port = 8800
socket.bind(('',port))

filename, addr = socket.recvfrom(1024)

data_transferred = 0
_data,addr = socket.recvfrom(1024)
print("file recv start from",addr[0])
print("File Name : ",filename.decode())
filesize = int(_data.decode())
print("File Size : ",filesize)

data,_ = socket.recvfrom(1024)
with open('receive file','wb') as f:
    while data:
        f.write(data)
        data_transferred += len(data)
        if filesize <= data_transferred:
            break
        data, _ = socket.recvfrom(1024)
        print("current_size / total_size = ",data_transferred,"/",filesize,",",(data_transferred/filesize)*100)

f.close()
socket.close()
print("file receive complete")

