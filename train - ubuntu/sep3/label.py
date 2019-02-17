import os
from random import shuffle

file_root = './'


def todo(string):
    file = open(file_root + string + '.txt', 'w')
    flist = []
    for i in range(0, 10):
        for f in os.listdir(file_root + string + '/c' + str(i)):
            flist.append(string + '/c' + str(i) + '/' + f + ' ' + str(i) + '\n')
            #file.write( string + '/c' + str(i) + '/' + f + ' ' + str(i) + '\n')
    shuffle(flist)
    print string, len(flist)
    for l in flist:
        file.write(l)
    file.close()


todo('train')
todo('test')
