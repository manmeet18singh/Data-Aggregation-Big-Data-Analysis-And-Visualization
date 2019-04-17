from nytimesarticle import articleAPI
import csv
import os.path
import time
import requests
from bs4 import BeautifulSoup
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize 
from nltk.stem import PorterStemmer 
import string
import re

def collectUrls(query, filename):
    api = articleAPI('aruVhl4pt0AUEOnD9LR7V1s4p7wavw9H')
    nytArt = None
    urls = []

    for pageNum in range(0,70):
        nytArt = api.search(q = query, 
                            fq = 'The New York Times', page = pageNum)
        print("loading page: %d" % pageNum)
        
        for article in nytArt['response']['docs']:
            urls.append(article['web_url'])
            # save sport article data to txt and write to txt in Data/nyt
        with open(os.path.join(filename), 'w') as txtFile:
            for url in urls: 
                txtFile.write(url + '\n')
        txtFile.close()
        print("going to sleep")
        time.sleep(6)
    print("\n\n\n ============ DONE COLLECTING " + query + " ============\n\n\n")


def collectArticles(readname, writename):
    sesh = requests.Session()
    webText = ''
    count = 1
    with open(os.path.join(readname)) as readFile:
        for line in readFile:
            article = sesh.get(line)
            soup = BeautifulSoup(article.text, 'html.parser')
            par = soup.find_all('p')
            with open(os.path.join(writename), 'w') as txtFile:
                for p in par: 
                    webText = webText + ' ' + p.get_text() 
                    txtFile.write(webText)
            txtFile.close()
            if (count% 50 == 0):
                print ('wrote: %d articles' % count)
            count += 1
    readFile.close()
    print("\n\n\n ============ DONE COLLECTING " + writename + " ============\n\n\n")


def cleanup(unclean, clean):
    count = 1
    stop_words = set(stopwords.words('english'))

    with open(os.path.join(unclean)) as uncleanArt:
        for line in uncleanArt:
            wordsToWrite = []
            words = word_tokenize(line)
            for word in words:
                if not word in stop_words:
                    if not (any(i.isdigit() for i in (word.split()[0]))):
                        word = re.sub(r'[^\w\s]','', word)
                        word = word.lower()
                        if not word in stop_words:       
                            wordsToWrite.append(word)
            with open(os.path.join(clean), 'a') as cleanArt:
                for cleanWord in wordsToWrite:
                    if not cleanArt in stop_words:
                        cleanArt.write(cleanWord + " ")
            cleanArt.close()
            if (count % 1000 == 0):
                print ('cleaned %d lines' % count)
            count += 1            
    uncleanArt.close()
    print("\n\n\n ============ DONE CLEANING " + clean + " ============\n\n\n")

def main():
    queryPath = {
                    'Basketball' : '../data/nyt/urls/basketball.txt',
                    'Baseball' : '../data/nyt/urls/baseball.txt', 
                    'Hockey' : '../data/nyt/urls/hockey.txt', 
                    'Football' : '../data/nyt/urls/football.txt', 
                    'Cricket' : '../data/nyt/urls/cricket.txt',
                    'Sport' : '../data/nyt/urls/sport.txt'}

    # allPaths = {
                # '../data/nyt/articles unclean/basketArt.txt' : '../data/nyt/urls/basketball.txt', 
                # '../data/nyt/articles unclean/baseArt.txt': '../data/nyt/urls/baseball.txt', 
                # '../data/nyt/articles unclean/hockeyArt.txt' : '../data/nyt/urls/hockey.txt', 
                # '../data/nyt/articles unclean/footArt.txt' : '../data/nyt/urls/football.txt', 
                # '../data/nyt/articles unclean/cricArt.txt' : '../data/nyt/urls/cricket.txt',
                # '../data/nyt/articles unclean/sportArt.txt' : '../data/nyt/urls/sport.txt'}
    cleaned = {
                '../data/nyt/articles unclean/basketArt.txt' : '../data/nyt/articles clean/basketball.txt', 
                '../data/nyt/articles unclean/baseArt.txt': '../data/nyt/articles clean/baseball.txt', 
                '../data/nyt/articles unclean/hockeyArt.txt' : '../data/nyt/articles clean/hockey.txt', 
                '../data/nyt/articles unclean/footArt.txt' : '../data/nyt/articles clean/football.txt', 
                '../data/nyt/articles unclean/cricArt.txt' : '../data/nyt/articles clean/cricket.txt',
                '../data/nyt/articles unclean/sportArt.txt' : '../data/nyt/articles clean/sport.txt'}

    # collect all the article urls
    # for query, path in queryPath.items():
        # collectUrls(query, path)

    # collect the actual articles
    # for write, read in allPaths.items():
        # collectArticles(read, write)

    # TODO: Make sure to add better stop words in nltk_data
    # clean up all the articles
    for unclean, clean in cleaned.items():
        cleanup(unclean, clean)

if __name__ == "__main__":
    main()
