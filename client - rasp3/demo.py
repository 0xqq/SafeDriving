import classify
import signal
from pygame import mixer
from time import sleep
from threading import Thread
from picamera import PiCamera
import client


def todo():
    print '[test.todo] Player init...'
    mixer.init()
    mixer.music.load('./data/warning.mp3')
    print '[test.todo] Player init done...'

    print '[test.todo] Classify init...'
    clf = classify.Clf()
    print '[test.todo] Classify init done...'

    print '[test.todo] Camera init...'
    camera = PiCamera()
    camera.resolution = (800, 800)
    camera.start_preview()
    print '[test.todo] Camera init done...'

    print '[test.todo] Client init...'
    client.client_init()
    print '[test.todo] Client init done...'

    while True:
        print '[test.todo] ****************************'
        print '[test.todo] Take picture...'
        camera.capture('./data/img.png', resize=(256, 256))
        print '[test.todo] Take picture done...'

        print '[test.todo] Send img...'
        client.send_pic()
        print '[test.todo] Send img done...'

        result = clf.classify_image('./data/img.png')
        print 'result: ', result[1]
        if result[0] and result[1] != '0 safe driving':
            mixer.music.play()
        sleep(2)
        print '[test.todo] ****************************'


if __name__ == "__main__":
    print '[main] Thread start...'
    try:
        signal.signal(signal.SIGINT, quit)
        signal.signal(signal.SIGTERM, quit)

        t = Thread(target=todo)
        t.setDaemon(True)
        t.start()
        #t.join()
        while True:
            sleep(1)
    except Exception, exc :
        client.client_close()
        print '[main] Thread end...'

#clf = classify.Clf()
#print clf.classify_image('./j.png')



