#!/usr/bin/env python3
import sys
 
words = []
wordTupCounts = []
neighbors = 2 

# Add all words to an array
for line in sys.stdin:
    line = line.strip()
    words2 = line.split()
    for word in words2:
        words.append(word)

# Loop through array, at each word, look at NEIGHBORS
for i in range(len(words)):
    if i == 0:
        tup = ((words[i], words[i+1]), 1)
        wordTupCounts.append(tup);
    elif i == len(words)-1:
        tup = ((words[i], words[i-1]), 1)
        wordTupCounts.append(tup);
    else:
        tup1 = ((words[i], words[i-1]), 1)
        tup2 = ((words[i], words[i+1]), 1)
        wordTupCounts.append(tup1)
        wordTupCounts.append(tup2)

for tup in wordTupCounts:
    print(str(tup[0]) + " " + str(tup[1]))
