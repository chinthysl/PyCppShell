#!/bin/bash
echo "First arg: $1"
echo "Second arg: $2"

wget -O dowloadContent.log -r $1
grep -a $2 dowloadContent.log
echo "Number of occurances of the word $2:" && grep -a $2 dowloadContent.log | wc -l
