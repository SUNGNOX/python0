import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('127.10.0.1', 9000))

print('wating for connect...')
data, addr = s.recvfrom(1024)
print(data.decode('utf-8'))
s.sendto(b'hello! I\'m UDP servies!!', addr)

data, addr = s.recvfrom(1024)
print(data.decode('utf-8'))