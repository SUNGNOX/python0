import socket, threading
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('127.0.0.1', 9999))#绑定


def udp(data, addr):
    print(threading.current_thread().name,('from %s:%s!' % addr))
    s.sendto(b'from %s!!' % data, addr)

while True:
    data, addr = s.recvfrom(1024)
    t=threading.Thread(target=udp, args=(data, addr))
    t.start()
    t.join()
