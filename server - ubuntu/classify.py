import numpy as np
caffe_root = '/home/kuma/caffe'
import sys
sys.path.insert(0, caffe_root + '/python')
import caffe
import matplotlib.pyplot as plt


model_def = caffe_root + '/models/bvlc_reference_caffenet/deploy.prototxt'
model_weights = caffe_root + '/models/bvlc_reference_caffenet/bvlc_reference_caffenet.caffemodel'
model_mean = caffe_root + '/python/caffe/imagenet/ilsvrc_2012_mean.npy'
labels_file = caffe_root + '/data/ilsvrc12/synset_words.txt' 


class Clf(object):
    def __init__(self):
        self.net = caffe.Net(model_def, model_weights, caffe.TEST)

        self.transformer = caffe.io.Transformer({'data': self.net.blobs['data'].data.shape})
        self.transformer.set_transpose('data', (2,0,1))
        mean = np.load(model_mean).mean(1).mean(1)
        self.transformer.set_mean('data', mean)
        self.transformer.set_raw_scale('data', 255) 
        self.transformer.set_channel_swap('data', (2,1,0))
        
        self.net.blobs['data'].reshape(50, 3, 227, 227)
        self.labels = np.loadtxt(labels_file, str, delimiter='\t')

    def classify_image(self, image):
        try:
            img = caffe.io.load_image(image)
            transformed_image = self.transformer.preprocess('data', img)
            plt.imshow(img)
            self.net.blobs['data'].data[...] = transformed_image

            output = self.net.forward()
            output_prob = output['prob'][0]
            top_inds = output_prob.argsort()[::-1][:5]

            return (True, self.labels[output_prob.argmax()], zip(output_prob[top_inds], self.labels[top_inds]))
        except Exception as err:
            logging.info('Classification error: %s', err)
            return (False, 'Something went wrong when classifying the '
                           'image. Maybe try another one?')

