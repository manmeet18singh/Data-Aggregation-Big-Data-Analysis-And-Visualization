#!/usr/bin/env python3
import sys
 
counts = {}
 
for line in sys.stdin:
    line = line.strip()
    word, count = line.split(' ', 1)
    count = int(count)

    if word in counts:
        counts[word] = counts[word] + count
    else:
        counts[word] = count
 
for word in counts.keys():
    print word + " " + str(counts[word])
