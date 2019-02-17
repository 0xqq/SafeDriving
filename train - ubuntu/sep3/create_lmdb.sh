#!/usr/bin/env sh


rm -rf ./train_lmdb
/home/bigmms/caffe/build/tools/convert_imageset ../ -shuffle ./train.txt ./train_lmdb
echo 'train_lmdb done'

rm -rf ./val_lmdb
/home/bigmms/caffe/build/tools/convert_imageset ../ -shuffle ./val.txt ./val_lmdb
echo 'val_lmdb done'

rm -rf ./mean.binaryproto
rm -rf ./mean.npy

/home/bigmms/caffe/build/tools/compute_image_mean ./train_lmdb ./mean.binaryproto
echo 'mean done'
