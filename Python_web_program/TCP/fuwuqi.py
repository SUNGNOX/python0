import socket
import threading

from threading import Thread
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('127.0.10.1', 4000))
s.listen(0)
print('waiting for connect......')
def tcplink(sock, addr):
    sock.send(b'welcome!!')
    print('%s' % threading.current_thread().name)
    print('connect from %s:%s !' % addr)
    while True:
        data = sock.recv(1024)
        if data:
            sock.send(('hello %s' % data.decode('utf-8')).encode('utf-8'))
        else:
            sock.close()
            break

while True:
    sock, addr = s.accept()
    # tcplink(sock, addr)
    t = Thread(target=tcplink, args=(sock, addr))
    t.start()
    t.join()


