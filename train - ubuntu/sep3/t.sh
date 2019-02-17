#!/usr/bin/env sh

for i in 0 1 2 3 4
do
  PT=./sec_$i
  echo $PT
  cp ./create_lmdb.sh $PT
  cp ./deploy.prototxt $PT
  cp ./train_val.prototxt $PT
  cp ./solver.prototxt $PT
  cp ./train.sh $PT
  pwd
  cd $PT
  pwd
  #./create_lmdb.sh
  cd ../
done
