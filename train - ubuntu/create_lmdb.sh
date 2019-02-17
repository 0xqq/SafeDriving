#!/usr/bin/env sh

python label.py

DATA=/home/kuma/pro

rm -rf $DATA/train_lmdb
/home/bigmms/caffe/build/tools/convert_imageset $DATA/imgs/train/ -shuffle $DATA/train.txt $DATA/imgs/train_lmdb
echo 'train_lmdb done'

rm -rf $DATA/test_lmdb
/home/bigmms/caffe/build/tools/convert_imageset $DATA/imgs/train/ -shuffle $DATA/test.txt $DATA/imgs/test_lmdb
echo 'test_lmdb done'

/home/bigmms/caffe/build/tools/compute_image_mean imgs/train_lmdb imgs/mean.binaryproto
