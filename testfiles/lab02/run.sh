#!/bin/bash

rm -rf output
mkdir output

for file in ./*
do
  #if [[ $file == *"sm"* && $file != *"5000"* && $file == *".in" && $file != *"worst"* ]]; then
  if [[ $file == *".dat" ]]; then
    fileTokens=(${file//./ })
    filename=${fileTokens[0]}
    filename=$( echo "$filename" | cut -c2- )
    datfile="${filename}.dat"
    infile="${filename}-test.in"
#    elapsed_time=$( TIMEFORMAT='%lU'; time (python2.7 runme2.py $datfile $infile > \ 
#                  output/${filename}-test.out 2> output/${filename}.paths) 2>&1 )
    echo "output for $file done in ${elapsed_time}."
  fi
done

echo "comparing outputs..."

for file in ./output/*; do
  if [[ $file == *".out" ]]; then
    generated_file=$( echo "$file" | cut -c3- )
    given_file=$( echo "$file" | cut -c10- )
    python2.7 compare.py "$given_file" "$generated_file"
  fi
done
