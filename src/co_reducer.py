#!/usr/bin/env python3
import sys
 
counts = {}
 
for line in sys.stdin:
    line = line.strip()
    # print(line)
    tup, count = line.split(' ', 1)
    tup1, tup2 = tup.split('|', 1)
    co = (tup1 + " " + tup2)
    co2 = (tup2 + " " + tup1)
    
    # print(counts)
    # print(co + " || " + co2)
    if co in counts:
        counts[co] = int(counts[co]) + int(count)
    elif co2 in counts:
        counts[co2] = int(counts[co2]) + int(count)
    else:
        counts[co] = int(count)
 
for tup in counts.keys():
    print(tup + " " + str(counts[tup]))
