caffe_root = '/home/bigmms/caffe'
import sys
sys.path.insert(0, caffe_root + '/python')
import caffe

import numpy as np

k = 5
for i in range(0, k):
    MEAN_PROTO_PATH = './sec_' + str(i) + '/mean.binaryproto'
    MEAN_NPY_PATH = './sec_' + str(i) + '/mean.npy'

    blob = caffe.proto.caffe_pb2.BlobProto()
    data = open(MEAN_PROTO_PATH, 'rb' ).read()
    blob.ParseFromString(data)

    array = np.array(caffe.io.blobproto_to_array(blob))
    mean_npy = array[0]
    np.save(MEAN_NPY_PATH ,mean_npy)
