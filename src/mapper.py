#!/usr/bin/env python3
import sys
 
for line in sys.stdin:
    line = line.strip()
    words = line.split()

    for word in words: 
        retVal = word + " " + str(1)
        print retVal
