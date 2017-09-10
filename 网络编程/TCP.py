import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('www.sina.com.cn', 80))
s.send(b'GET / HTTP/1.1\r\nHOST: www.sina.com.cn\r\nConnection: close\r\n\r\n')
buff = []
while True:
    a = s.recv(1024)
    if a:
        buff.append(a)
    else:
        break

sina = b''.join(buff)
f = open('TCP.html', 'wb')
f.write(sina)
f.close()
#Sina = sina.split('0')
s.close()

#************************************************************