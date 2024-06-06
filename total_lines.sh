#!/bin/bash

total_lines=0

for file in *.txt
do
  line_count=$(wc -l < "$file") 
  total_lines=$((total_lines + line_count))
done

echo "--total_lines--"
echo "Total number of lines in all 10 books: $total_lines"
