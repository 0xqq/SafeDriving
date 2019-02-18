import socket
import threading
import time
import os
import matplotlib.pyplot as plt
from datetime import datetime


HOST = '0.0.0.0'
PORT = 5000


def recv_image(sock):
    
    root = './image/img-' + str(datetime.now().strftime('%Y-%m-%d-%H-%M-%S')) + '.png'
    print 'Create file ...'
    with open(root, 'wb') as f: pass
    
    size = int(sock.recv(1024))
    s = 0
    while size > s:
        data = sock.recv(1024)
        s += len(data)
        with open(root, 'ab') as f:
            f.write(data)
    print 'data received'


def connect(sock, addr):

    print 'Accept new connection from %s:%s...' % addr

    sock.send('hello client')
    print sock.recv(1024)
    print 'Communication success'

    print 'Begin to save image ...'
    os.system('rm -r ./image/*.png')
    while True:
        recv_image(sock)
    print 'Finished saving image ...'

    sock.close()


if __name__ == '__main__':

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    s.bind((HOST, PORT))

    s.listen(1)

    print 'Waiting for connection...'
    while True:
        sock, addr = s.accept()
        threading.Thread(target = connect, args = (sock, addr)).start()

    s.close()

