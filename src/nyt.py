from nytimesarticle import articleAPI
import csv
import os.path
import time

api = articleAPI('aruVhl4pt0AUEOnD9LR7V1s4p7wavw9H')

# collect articles with March Madness Keyword
# mmArt = None
# mmUrlCsv = ['url']

# for pageNum in range(0, 70):
#     mmArt = api.search(q = 'March Madness',
#                     fq = 'The New York Times', page = pageNum)
#     # save mmArticle to csv format
#     for article in mmArt['response']['docs']:
#         mmUrlCsv.append(article['web_url'])
#         time.sleep(6)

# # save mm data to csv and write to csv in Data/nyt/
# fileName = os.path.join('../Data/nyt/mmUrl.csv')
# with open(fileName, 'w') as csvFile:
#     writer = csv.writer(csvFile)
#     for url in mmUrlCsv: 
#         writer.writerow([url])
# csvFile.close()

##########################################################################################################################

# Collect articles with sport keyword
sportArt = None
sportUrlCsv = ['url']

# collect articles with keywords Sport or Sports
sportArt = api.search(q = ['Sport', 'Sports'], 
                        fq = {'headline' : ['Sport', 'Sports'], 'body':['Sport', 'Sports']})





# save sport article data to csv and write to csv in Data/nyt
fileName = os.path.join('../Data/nyt/sportUrl.csv')
with open(fileName, 'w') as csvFile:
    writer = csv.writer(csvFile)
    for url in mmUrlCsv: 
        writer.writerow([url])
csvFile.close()