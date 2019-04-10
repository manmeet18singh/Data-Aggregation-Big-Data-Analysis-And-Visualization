# Reads in a word counted file (wordCount_phase1.txt) and does more post-processing on it

import nltk
from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
import string
import re

stop_words = set(stopwords.words('english'))

ps = PorterStemmer()

all_words = []

def removeNums(file):
    good_words = []
    with open(file, "r") as f:
        for line in f:
            if not (any(i.isdigit() for i in (line.split()[0]))):
                good_words.append(line)
        f.close()
    f = open(file + ".NUMS", "w")
    for word in good_words:
        f.write(word)
    f.close()

def main():
    f = open('sportingnews_extracted.txt', "r")
        # for line in f:
            # Grab word
            # word = line.split()[0]
    garbage = f.read()
    words = garbage.split()
    for word in words:
        # Make lowercase
        word = word.lower()
        # Check if stop word
        if word != stop_words:
            # Stem word and add it to set
            ps.stem(word)
            word = re.sub(r'[^\w\s]','',word)
            all_words.append(word)
    file = open('sportingnews_cleaned.txt', "w")
    for word in all_words:
        file.write(word + " ")
    file.close()

if __name__== "__main__":
  removeNums("../data/cc/bleacher/bleacher_wordCount_sorted.txt")
  removeNums("../data/cc/cbs/cbs_wordCount_sorted.txt")
  removeNums("../data/cc/espn/espn_wordCount_sorted.txt")
  removeNums("../data/cc/fox/fox_wordCount_sorted.txt")
  removeNums("../data/cc/sporting/sportingnews_wordCount_sorted.txt")