# Reads in a word counted file and sorts it (ascending)

import nltk
from nltk.corpus import stopwords

stop_words = set(stopwords.words('english'))

def main():
    word_tups = []
    with open('../data/nyt/wc-run.txt', "r") as f:
        for line in f:
            text = line.split()
            word = text[0]
            count = int(text[1])
            tup = (word, count)
            word_tups.append(tup)
        f.close()

    sorted_words = sorted(word_tups, key=lambda x: x[1])
    sorted_words.reverse()

    file = open("../data/nyt/wc-run.txt", "w")
    for tup in sorted_words:
        if tup[0] not in stop_words:
            file.write(tup[0] + " " + str(tup[1]) + "\n")
    file.close()

if __name__== "__main__":
  main()