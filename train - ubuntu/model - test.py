import classify
import os


caffe_root = '/home/bigmms/caffe/'
img_root = './other/'
import sys
sys.path.insert(0, caffe_root + 'python')
import caffe


clf = classify.Clf()
#print clf.classify_image('./img_1197.png)
label = []
with open('./word.txt', 'r') as f:
    tamp = f.readline()
    while tamp:
        label.append(tamp[:-1])
        tamp = f.readline()
total = 0
succ = 0
for i in range(0,10):
    root = img_root + 'c' + str(i) + '/'
    for f in os.listdir(root):
        total += 1
        result = clf.classify_image(root + f)
        if result[1] == label[i]:
            succ += 1
        #print label[i], result
    print 'iter_' + str(i), succ, total, float(succ) / float(total)
print succ, total, float(succ) / float(total)

