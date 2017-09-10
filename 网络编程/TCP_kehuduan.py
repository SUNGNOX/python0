import socket
import time
# s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1', 5000))
print(s.recv(1024).decode('utf-8'))
data = [b'Tom', b'Jack', b'water']
for name in data:
    s.send(name)
    # s.sendto(name, ('127.0.0.1', 9999))
    print(s.recv(1024).decode('utf-8'))

time.sleep(20)
s.close()
