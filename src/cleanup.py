import os.path
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize 
from nltk.stem import PorterStemmer 
import string
import re

def cleanup(unclean, clean):
    count = 1
    stop_words = set(stopwords.words('english'))

    with open(os.path.join(unclean)) as unClean:
        # read line by line of the unclean data
        for line in unClean:
            wordsToWrite = []

            #  use nltk to tokenize every word in current line
            words = word_tokenize(line)
            for word in words:
                # check if word is a stop word, digit or symbol axe them 
                # and convert into lower case and hold onto them
                if not word in stop_words:
                    if not (any(i.isdigit() for i in (word.split()[0]))):
                        word = re.sub(r'[^\w\s]','', word)
                        word = word.lower()
                        if not word in stop_words:       
                            wordsToWrite.append(word)

            # write the cleaned up words to txt 
            with open(os.path.join(clean), 'a') as cleanedUp:
                
                # just checking one more time for stop words
                for cleanWord in wordsToWrite:
                    if not cleanedUp in stop_words:
                        cleanedUp.write(cleanWord + " ")
            cleanedUp.close()

            # prints for sanity
            if (count % 1000 == 0):
                print ('cleaned %d lines' % count)
            count += 1            
    unClean.close()
    print("\n\n\n ============ DONE CLEANING " + clean + " ============\n\n\n")

def main():
    # path of the txt file, path of where to save the txt file 
    # CALL THIS:
    cleanup( '../data/demo/pg345.txt' , '../data/demo/clean.txt')

if __name__ == "__main__":
    main()
