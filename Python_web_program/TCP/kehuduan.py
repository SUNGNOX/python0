import socket
import time
#链接网络
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('www.sina.com', 80))
s.send(b'GET / HTTP/1.1\r\nHost: www.sina.com\r\nConnection: close\r\n\r\n')
buf = []
while True:
    data = s.recv(1024)
    if data:
        buf.append(data)
        print(data.decode('utf-8'))
    else:
        break
s.close()
#链接本地服务器
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.10.1', 4000))
print(s.recv(1024).decode('utf-8'))
s.send(b'abc')
print(s.recv(1024).decode('utf-8'))
s.send(b'abc')
print(s.recv(1024).decode('utf-8'))
s.send(b'abc')
print(s.recv(1024).decode('utf-8'))
time.sleep(20)
s.close()
