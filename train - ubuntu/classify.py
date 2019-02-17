import numpy as np
caffe_root = '/home/bigmms/caffe'
import sys
sys.path.insert(0, caffe_root + '/python')
import caffe
import matplotlib.pyplot as plt


model_def = './deploy.prototxt'
model_weights = './sep3_iter_5000.caffemodel'
model_mean = './mean.npy'
labels_file = './word.txt'


class Clf(object):
    def __init__(self):
        self.net = caffe.Net(model_def, model_weights, caffe.TEST)

        self.transformer = caffe.io.Transformer({'data': self.net.blobs['data'].data.shape})
        self.transformer.set_transpose('data', (2,0,1))
        mean = np.load(model_mean).mean(1).mean(1)
        self.transformer.set_mean('data', mean)
        self.transformer.set_raw_scale('data', 255)
        self.transformer.set_channel_swap('data', (2,1,0))

        self.net.blobs['data'].reshape(1, 3, 256, 256)
        self.labels = np.loadtxt(labels_file, str, delimiter='\t')

    def classify_image(self, image):
        try:
            img = caffe.io.load_image(image)
            transformed_image = self.transformer.preprocess('data', img)
            #plt.imshow(img)
            self.net.blobs['data'].data[...] = transformed_image

            output = self.net.forward()
            output_prob = output['prob'][0]
            top_inds = output_prob.argsort()[::-1][:5]

            return (True, self.labels[output_prob.argmax()], zip(output_prob[top_inds], self.labels[top_inds]))
        except Exception as err:
            #logging.info('Classification error: %s', err)
            return (False, 'Something went wrong when classifying the '
                           'image. Maybe try another one?')

