import tweepy
import csv
import os.path
import time

# set up Twitter api key info
auth = tweepy.AppAuthHandler('oWiSM7BuSqq9Je0rddAWAyRDI','FY7I9s4xRkdbIIvSSXivZ948HJn3zd6m2C70rwFEenzEOI7kvK')
# auth.set_access_token('1096150810478735360-yP5Z5pScHIGoGB0x4gPPaz06Yiqk3F','dpSSg6z3Kh5Xo3Abdg3CBtwefBI2AOEAszXSzCTMPjnua')

api = tweepy.API(auth, wait_on_rate_limit = True, wait_on_rate_limit_notify = True)

# Rate Limit Handler, restart every 15 mins after rate limit is exceeded
def limitHandler(cursor):
    while True:
        try:
            yield cursor.next()
        except tweepy.TweepError:
            time.sleep(15*60)


searchQuery = 'March Madness OR #marchmadness'
maxTweets = 80000

tweetId = None
numTweets = 0
csvData = [['Created At', 'Text', 'Name']]

# search on Twitter with Keyword: March Madness, retrieve tweets
for tweet in limitHandler(tweepy.Cursor(api.search, q = searchQuery).items(maxTweets)):
    csvData.append([tweet.created_at.strftime("%m/%d/%Y"),tweet.text,tweet.user.name])
    numTweets += 1
    print("Downloaded {0} tweets".format(numTweets))

# save data to csv and write to csv in Data/tw/
fileName = os.path.join('../Data/tw/tweets.csv')
with open(fileName, 'w') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerows(csvData)
csvFile.close()