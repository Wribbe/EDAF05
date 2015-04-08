#!/bin/bash

rm -rf output
mkdir output

for file in ./*
do
  #if [[ $file == *"sm"* && $file != *"5000"* && $file == *".in" && $file != *"worst"* ]]; then
  if [[ $file == *"sm"* && $file != *"5000"* && $file == *".in" ]]; then
    fileTokens=(${file//./ })
    filename=${fileTokens[0]}
    filename=$( echo "$filename" | cut -c2- )
    java Runme $file > output/${filename}.out
    echo "output for $file done."
  fi
done

echo "comparing outputs..."

for file in ./output/*; do
  generated_file=$( echo "$file" | cut -c3- )
  given_file=$( echo "$file" | cut -c10- )
  java Compare "$given_file" "$generated_file"
done
