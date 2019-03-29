import tweepy
import csv
import os.path
import time

# set up Twitter api key info
auth = tweepy.AppAuthHandler('oWiSM7BuSqq9Je0rddAWAyRDI','FY7I9s4xRkdbIIvSSXivZ948HJn3zd6m2C70rwFEenzEOI7kvK')

api = tweepy.API(auth, wait_on_rate_limit_notify = True)

# Rate Limit Handler, restart every 15 mins after rate limit is exceeded
def limitHandler(cursor):
    firstWrite = False

    while True:
        try:
            yield cursor.next()
        except (tweepy.TweepError, StopIteration):
            print('hit rate limit ... saved this batch to csv ... sleeping for 15 mins')
            
            # save data to csv and write to csv in Data/tw/
            if (not firstWrite):
                fileName = os.path.join('../Data/tw/tweets.csv')
                with open(fileName, 'w') as csvFile:
                    writer = csv.writer(csvFile)
                    writer.writerows(csvData)
                    firstWrite = True
                csvFile.close()
            else:
                fileName = os.path.join('../Data/tw/tweets.csv')
                with open(fileName, 'a') as csvFile:
                    writer = csv.writer(csvFile)
                    writer.writerows(csvData)
                csvFile.close()
            time.sleep(15*60)
 

searchQuery = 'March Madness OR #marchmadness'
maxTweets = 60000

tweetId = None
numTweets = 0
csvData = [['Created At', 'Text', 'Name']]

# search on Twitter with Keyword: March Madness, retrieve tweets
for tweet in limitHandler(tweepy.Cursor(api.search, q = searchQuery).items(maxTweets)):
    if ('RT @' not in tweet.text):
        csvData.append([tweet.created_at.strftime("%m/%d/%Y"),tweet.text,tweet.user.name])
        numTweets += 1
        if (numTweets%1000 == 0):
            print("Downloaded {0} tweets".format(numTweets))