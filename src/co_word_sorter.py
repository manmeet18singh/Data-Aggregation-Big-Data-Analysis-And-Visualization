# Reads in a word counted file and sorts it (ascending)

import nltk
from nltk.corpus import stopwords

stop_words = set(stopwords.words('english'))

def main():
    word_tups = []
    with open('../data/tw/co_occ/hockey.txt', "r") as f:
        for line in f:
            text = line.split()
            word1 = text[0]
            word2 = text[1]
            count = int(text[2])
            tup = ((word1 + " " + word2), count)
            if word1 not in stop_words and word2 not in stop_words:
                if not (any(i.isdigit() for i in word1)):
                    if not (any(i.isdigit() for i in word2)):
                        word_tups.append(tup)
        f.close()

    sorted_words = sorted(word_tups, key=lambda x: x[1])
    sorted_words.reverse()

    file = open("../data/tw/co_occ/hockey_sorted.txt", "w")
    for tup in sorted_words:
        file.write(tup[0] + " " + str(tup[1]) + "\n")
    file.close()

if __name__== "__main__":
  main()