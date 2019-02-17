import socket
import time
import os


HOST = '192.168.1.106'
PORT = 5000
s = None


def client_init():
    print '[client.client_init] Client init...'
    global s
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((HOST, PORT))
    except socket.error, msg:
        print msg
        sys.exit()

    print s.recv(1024)

    s.send('hello server')
    print '[client.client_init] Client init done...'
    time.sleep(0.5)


def send_pic():
    global s
    print '[client.send_pic] command begins ...'

    print '[client.send_pic] sending, please wait for a second ...'

    size = os.path.getsize('./data/img.png')
    s.send(str(size))
    time.sleep(0.5)

    with open('./data/img.png', 'rb') as f:
        for data in f:
            s.send(data)
    print '[client.send_pic] send done...'

    time.sleep(0.5)


def client_close():
    global s
    s.close()
    print '[client.client_close] connection closed'

#client_init()
#send_pic()
#client_close()
