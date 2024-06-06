#!/bin/bash

total_words=0

for file in *.txt
do
  word_count=$(wc -w < "$file")
  total_words=$((total_words + word_count))
done

echo "--total_words--"
echo "Total number of words in all 10 books: $total_words"
