from nytimesarticle import articleAPI
import csv
import os.path
import time
import requests
from bs4 import BeautifulSoup

def collectUrls(query, filename):
    api = articleAPI('aruVhl4pt0AUEOnD9LR7V1s4p7wavw9H')
    # Collect articles with keyword
    # basketballArt = None
    nytArt = None
    # basketballTxt = []
    urls = []

    for pageNum in range(0,70):
        nytArt = api.search(q = query, 
                            fq = 'The New York Times', page = pageNum)
        print("loading page: %d" % pageNum)
        
        for article in nytArt['response']['docs']:
            urls.append(article['web_url'])
            # save sport article data to txt and write to txt in Data/nyt
            # fileName = os.path.join('../Data/nyt/basketball.txt')
        with open(os.path.join(filename), 'w') as txtFile:
            for url in urls: 
                txtFile.write(url + '\n')
        txtFile.close()
        print("going to sleep")
        time.sleep(6)
    print("\n\n\n ============ DONE COLLECTING " + query + " ============\n\n\n")


def collectArticles(readname, writename):
    with open(os.path.join(readname)) as readFile:  
        for line in readFile:
            
            # TODO: READ LINE BY LINE AND MAKE A URL REQUEST AND GRAB THE ARTICLE TEXT USING BEAUTIFULL SOUP. 
            # PASS INTO FUNCTIONS TO CLEAN UP STOP WORDS AND STEM WORDS
            print(line)
        # with open(os.path.join(writename), 'w') as article:
        #     for tweet in reader:
        #         print(tweet[])
        #         # tweetTxt.write(tweet['Text'].replace('\n', "") + '\n')
        #     tweetTxt.close()
    readFile.close()


def main():
    queryPath = { 'Basketball' : '../data/nyt/basketball.txt',
                    'Baseball' : '../data/nyt/baseball.txt', 
                    'Hockey' : '../data/nyt/hockey.txt', 
                    'Football' : '../data/nyt/football.txt', 
                    'Cricket' : '../data/nyt/cricket.txt'}

    allPaths = {'../data/nyt/basketArt.txt' : '../data/nyt/basketball.txt', 
                '../data/nyt/baseArt.txt': '../data/nyt/baseball.txt', 
                '../data/nyt/hockeyArt.txt' : '../data/nyt/hockey.txt', 
                '../data/nyt/footArt.txt' : '../data/nyt/football.txt', 
                '../data/nyt/cricArt.txt' : '../data/nyt/cricket.txt'}

    # for query, path in queryPath.items():
        # collectUrls(query, path)

    for write, read in allPaths.items():
        collectArticles(read, write)

if __name__ == "__main__":
    main()
