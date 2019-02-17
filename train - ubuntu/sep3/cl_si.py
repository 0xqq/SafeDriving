import os
from random import shuffle


def get_flist():

    flist = []
    tlist = []
    for i in range(0, 10):
        fi = os.listdir('./all/c' + str(i))
        tsize = int(0.02 * len(fi))
        shuffle(fi)
        for j in range(0, len(fi)):
            if j < tsize:
                tlist.append(('./all/c' + str(i) + '/' + fi[j], i))
            else:
                flist.append('./all/c' + str(i) + '/' + fi[j] + ' ' + str(i) + '\n')
    shuffle(flist)
    with open('./test.txt','w') as f:
        f.write(str(tlist))

    print len(flist), len(tlist)
    return flist


def set_label(flist, k):
    all_size = len(flist)
    sec_size = int(all_size / k)
    print all_size, sec_size
    sl = []
    pos = 0
    for i in range(0, k):
        if i != k - 1:
            sl.append([sec_size * pos, sec_size * (pos + 1)])
        else:
            sl.append([sec_size * pos, all_size])
        pos += 1
    print sl

    for i in range(0, k):
        root = './sec_' + str(i) + '/'
        os.system('rm -rf ' + root)
        os.mkdir(root)
        train_root = root + 'train.txt'
        val_root = root + 'val.txt'

        val_f = open(val_root, 'w')
        train_f = open(train_root, 'w')

        for j in range(0, len(flist)):
            if j >= sl[i][0] and j < sl[i][1]:
                val_f.write(flist[j])
            else:
                train_f.write(flist[j])
        val_f.close()
        train_f.close()


if __name__ =='__main__':
    k = 5
    set_label(get_flist(), k)
    #os.system('python mean.py')




