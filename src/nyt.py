from nytimesarticle import articleAPI
import csv
import os.path
import time

api = articleAPI('aruVhl4pt0AUEOnD9LR7V1s4p7wavw9H')

# # Collect articles with sport keyword
# sportArt = None
# sportCsv = []

# for pageNum in range(0,70):
#     sportArt = api.search(q = 'Sports', 
#                         fq = 'The New York Times', page = pageNum)
#     print("loading page: %d" % pageNum)
#     for article in sportArt['response']['docs']:
#         sportCsv.append(article['web_url'])
#         # save sport article data to csv and write to csv in Data/nyt
#     fileName = os.path.join('../Data/nyt/sport.csv')
#     with open(fileName, 'w') as csvFile:
#         writer = csv.writer(csvFile)
#         for url in sportCsv: 
#             writer.writerow([url])
#     csvFile.close()
#     print("going to sleep")
#     time.sleep(6)


# print("\n\n\nDONE COLLECTING SPORT\n\n\n")
##########################################################################################################################

# collect articles with Basketball Keyword
basketballArt = None
basketballCsv = []

for pageNum in range(0,70):
    basketballArt = api.search(q = 'Basketball', 
                        fq = 'The New York Times', page = pageNum)
    print("loading page: %d" % pageNum)
    for article in basketballArt['response']['docs']:
        basketballCsv.append(article['web_url'])
        # save sport article data to csv and write to csv in Data/nyt
    fileName = os.path.join('../Data/nyt/basketball.csv')
    with open(fileName, 'w') as csvFile:
        writer = csv.writer(csvFile)
        for url in basketballCsv: 
            writer.writerow([url])
    csvFile.close()
    print("going to sleep")
    time.sleep(6)


print("\n\n\nDONE COLLECTING BASKETBALL\n\n\n")
##########################################################################################################################

# collect articles with Baseball Keyword
baseballArt = None
baseballCsv = []

for pageNum in range(0,70):
    baseballArt = api.search(q = 'Baseball', 
                        fq = 'The New York Times', page = pageNum)
    print("loading page: %d" % pageNum)
    for article in baseballArt['response']['docs']:
        baseballCsv.append(article['web_url'])
        # save sport article data to csv and write to csv in Data/nyt
    fileName = os.path.join('../Data/nyt/baseball.csv')
    with open(fileName, 'w') as csvFile:
        writer = csv.writer(csvFile)
        for url in baseballCsv: 
            writer.writerow([url])
    csvFile.close()
    print("going to sleep")
    time.sleep(6)


print("\n\n\nDONE COLLECTING BASEBALL\n\n\n")
##########################################################################################################################

# collect articles with Hockey Keyword
hockeyArt = None
hockeyCsv = []

for pageNum in range(0,70):
    hockeyArt = api.search(q = 'Hockey', 
                        fq = 'The New York Times', page = pageNum)
    print("loading page: %d" % pageNum)
    for article in hockeyArt['response']['docs']:
        hockeyCsv.append(article['web_url'])
        # save sport article data to csv and write to csv in Data/nyt
    fileName = os.path.join('../Data/nyt/hockey.csv')
    with open(fileName, 'w') as csvFile:
        writer = csv.writer(csvFile)
        for url in hockeyCsv: 
            writer.writerow([url])
    csvFile.close()
    print("going to sleep")
    time.sleep(6)


print("\n\n\nDONE COLLECTING HOCKEY\n\n\n")
##########################################################################################################################

# collect articles with Football Keyword
footballArt = None
footballCsv = []

for pageNum in range(0,70):
    footballArt = api.search(q = 'Football', 
                        fq = 'The New York Times', page = pageNum)
    print("loading page: %d" % pageNum)
    for article in footballArt['response']['docs']:
        footballCsv.append(article['web_url'])
        # save sport article data to csv and write to csv in Data/nyt
    fileName = os.path.join('../Data/nyt/football.csv')
    with open(fileName, 'w') as csvFile:
        writer = csv.writer(csvFile)
        for url in footballCsv: 
            writer.writerow([url])
    csvFile.close()
    print("going to sleep")
    time.sleep(6)


print("\n\n\nDONE COLLECTING FOOTBALL\n\n\n")
##########################################################################################################################

# collect articles with Soccer Keyword
soccerArt = None
soccerCsv = []

for pageNum in range(0,70):
    soccerArt = api.search(q = 'soccer', 
                        fq = 'The New York Times', page = pageNum)
    print("loading page: %d" % pageNum)
    for article in soccerArt['response']['docs']:
        soccerCsv.append(article['web_url'])
        # save sport article data to csv and write to csv in Data/nyt
    fileName = os.path.join('../Data/nyt/soccer.csv')
    with open(fileName, 'w') as csvFile:
        writer = csv.writer(csvFile)
        for url in soccerCsv: 
            writer.writerow([url])
    csvFile.close()
    print("going to sleep")
    time.sleep(6)


print("\n\n\nDONE COLLECTING SOCCER\n\n\n")
##########################################################################################################################