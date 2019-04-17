#!/usr/bin/env python3
import sys
 
counts = {}
 
for line in sys.stdin:
    line = line.strip()
    print(line)
    tup, count = line.split(' ', 1)
    
    if tup in counts:
        counts[tup] = counts[tup] + count
    else:
        counts[tup] = count
 
for tup in counts.keys():
    print(str(tup) + " " + str(counts[tup]))
