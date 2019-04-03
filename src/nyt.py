from nytimesarticle import articleAPI
import csv
import os.path
import time

api = articleAPI('aruVhl4pt0AUEOnD9LR7V1s4p7wavw9H')

# collect articles with March Madness Keyword
mmArt = None
mmUrlCsv = ['url']

for pageNum in range(0,70):
    mmArt = api.search(q = 'March Madness', 
                        fq = 'The New York Times', page = pageNum)
    print("loading page: %d" % pageNum)
    for article in mmArt['response']['docs']:
        mmUrlCsv.append(article['web_url'])
        # save sport article data to csv and write to csv in Data/nyt
    fileName = os.path.join('../Data/nyt/mmUrl.csv')
    with open(fileName, 'w') as csvFile:
        writer = csv.writer(csvFile)
        for url in mmUrlCsv: 
            writer.writerow([url])
    csvFile.close()
    print("going to sleep")
    time.sleep(6)


print("\n\n\nDONE COLLECTING MARCH MADNESS\n\n\n")
##########################################################################################################################

# Collect articles with sport keyword
sportArt = None
sportUrlCsv = ['url']

for pageNum in range(0,70):
    sportArt = api.search(q = 'Sports', 
                        fq = 'The New York Times', page = pageNum)
    print("loading page: %d" % pageNum)
    for article in sportArt['response']['docs']:
        sportUrlCsv.append(article['web_url'])
        # save sport article data to csv and write to csv in Data/nyt
    fileName = os.path.join('../Data/nyt/sportUrl.csv')
    with open(fileName, 'w') as csvFile:
        writer = csv.writer(csvFile)
        for url in sportUrlCsv: 
            writer.writerow([url])
    csvFile.close()
    print("going to sleep")
    time.sleep(6)
