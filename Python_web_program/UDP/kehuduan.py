import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

s.sendto(b'hi', ('127.10.0.1', 9000))
data = s.recv(1024)
print(data.decode('utf-8'))

s.sendto(b'hi again!', ('127.10.0.1', 9000))

s.close()

