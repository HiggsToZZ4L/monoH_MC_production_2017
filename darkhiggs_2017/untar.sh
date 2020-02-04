#!/bin/bash
FILES=*.gz
for f in $FILES
do
  echo "Extracting $f file..."
  gunzip $f
done
