import socket
data = [b'mall', b'cat', b'dog', b'1', b'2', b'3']
for n in data:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('127.0.0.1', 9999))
    print((s.recv(1024)).decode('utf-8'))
    s.send(n)
#    s.sendto(n, ('127.0.0.1', 9999))
    print((s.recv(1024)).decode('utf-8'))
    s.close()