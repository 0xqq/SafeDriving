#!/bin/bash


file='9.jpg'
echo /a/a/$1/ddd
convert "$file" -crop 400x400+0+0 -resize 256x256 "${file%.*}_bl.png"
convert "$file" -crop 400x400+120+0 -resize 256x256 "${file%.*}_bc.png"
convert "$file" -crop 400x400+240+0 -resize 256x256 "${file%.*}_br.png"

convert "$file" -crop 400x400+0+80 -resize 256x256 "${file%.*}_cl.png"
convert "$file" -crop 400x400+120+80 -resize 256x256 "${file%.*}_cc.png"
convert "$file" -crop 400x400+240+80 -resize 256x256 "${file%.*}_cr.png"


