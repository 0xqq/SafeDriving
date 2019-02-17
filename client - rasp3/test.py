import classify
caffe_root = '/home/pi/caffe/'
img_root = './other/'
import sys
sys.path.insert(0, caffe_root + 'python')
import caffe


clf = classify.Clf()
print clf.classify_image('./img_17152_c.png')
