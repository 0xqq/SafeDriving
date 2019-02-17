#!/bin/bash

#simple script for resizing images in all class directories
#also reformats everything from whatever to png

if [ `ls test/*/*.jpg 2> /dev/null | wc -l ` -gt 0 ]; then
  echo hi
  for file in test/*/*.jpg; do
    convert "$file" -crop 480x480+0+0 "${file%.*}_l.png"
    convert "${file%.*}_l.png" -resize 256x256\! "${file%.*}_l.png"
    convert "$file" -crop 480x480+80+0 "${file%.*}_c.png"
    convert "${file%.*}_c.png" -resize 256x256\! "${file%.*}_c.png"
    convert "$file" -crop 480x480+160+0 "${file%.*}_r.png"
    convert "${file%.*}_r.png" -resize 256x256\! "${file%.*}_r.png"
    file "$file" #uncomment for testing
    rm "$file"
  done
fi

if [ `ls train/*/*.jpg 2> /dev/null | wc -l ` -gt 0 ]; then
  echo hi
  for file in train/*/*.jpg; do
    convert "$file" -crop 480x480+0+0 "${file%.*}_l.png"
    convert "${file%.*}_l.png" -resize 256x256\! "${file%.*}_l.png"
    convert "$file" -crop 480x480+80+0 "${file%.*}_c.png"
    convert "${file%.*}_c.png" -resize 256x256\! "${file%.*}_c.png"
    convert "$file" -crop 480x480+160+0 "${file%.*}_r.png"
    convert "${file%.*}_r.png" -resize 256x256\! "${file%.*}_r.png"
    file "$file" #uncomment for testing
    rm "$file"
  done
fi

if [ `ls other/*/*.jpg 2> /dev/null | wc -l ` -gt 0 ]; then
  echo hi
  for file in other/*/*.jpg; do
    convert "$file" -crop 480x480+0+0 "${file%.*}_l.png"
    convert "${file%.*}_l.png" -resize 256x256\! "${file%.*}_l.png"
    convert "$file" -crop 480x480+80+0 "${file%.*}_c.png"
    convert "${file%.*}_c.png" -resize 256x256\! "${file%.*}_c.png"
    convert "$file" -crop 480x480+160+0 "${file%.*}_r.png"
    convert "${file%.*}_r.png" -resize 256x256\! "${file%.*}_r.png"
    file "$file" #uncomment for testing
    rm "$file"
  done
fi

