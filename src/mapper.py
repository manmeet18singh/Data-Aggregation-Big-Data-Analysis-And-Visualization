#!/usr/bin/env python
import sys
 
for line in sys.stdin:
    #--- remove leading and trailing whitespace---
    line = line.strip()

    #--- split the line into words ---
    words = line.split()

    for word in words: 
        #print '%s\t%s' % (word, "1")
        retVal = word + " " + str(1)
        print retVal
