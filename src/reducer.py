#!/usr/bin/env python

import sys
 
# maps words to their counts
wordCounts = {}
 
# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
 
    # parse the input we got from mapper.py
    word, count = line.split(' ', 1)
    count = int(count)

    # If wordCount is not 0, add it. Else, set it
    if word in wordCounts:
        wordCounts[word] = wordCounts[word] + count
    else:
        wordCounts[word] = count
 
# write to stdout
for word in wordCounts.keys():
    print word + " " + str(wordCounts[word])
