import socket
import time
import threading

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('127.0.0.1', 9999))
s.listen(5)
print('wating for connect!!!')


def tcplink(sock, addr):
    n = 0
    print('tcplink: ', threading.current_thread().name)
    print('connecting from %s:%s' % addr)
    sock.send(b'welcome!!')
    while True:
        print('while: ', threading.current_thread().name)
        n=n+1
        print(n)
        a = sock.recv(1024)
        time.sleep(1)
        if not a or a.decode('utf-8') == 'exit':
            break
        sock.send(('hello %s!!' % a.decode('utf-8')).encode('utf-8'))
    sock.close()


while True:
    sock, addr = s.accept()
    print('connecting successful!!!')
    t = threading.Thread(target=tcplink, args=(sock, addr))
 #   t0 = threading.Thread(target=tcplink, args=(sock, addr), name='thread_t0')
 #    t.start()
  #  t0.start()
 #   t.join(1)
  #  t0.join()
