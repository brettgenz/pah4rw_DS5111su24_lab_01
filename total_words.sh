#!/bin/bash

total_words=cat *.txt | wc -w

echo "--total_words--"
echo "Total number of words in all 10 books: $total_words"
