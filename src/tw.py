import tweepy
import csv
import os.path
import time

# set up Twitter api key info
auth = tweepy.AppAuthHandler('oWiSM7BuSqq9Je0rddAWAyRDI','FY7I9s4xRkdbIIvSSXivZ948HJn3zd6m2C70rwFEenzEOI7kvK')
api = tweepy.API(auth)

# Rate Limit Handler, restart every 15 mins after rate limit is exceeded
def limitHandler(cursor, filename, firstWrite):
    numTweets = 0
    csvData = [['Created At', 'Text', 'Name']]
    while True:
        try:
            for tweet in cursor:
                if ('RT @' not in tweet.full_text and numTweets <= 10000):
                    csvData.append([tweet.created_at.strftime("%m/%d/%Y"),tweet.full_text,tweet.user.name])
                    numTweets += 1
                    if (numTweets%1000 == 0):
                        print("Downloaded {0} tweets".format(numTweets))
                if(numTweets > 10000):
                    if (not firstWrite):
                        with open(filename, 'w') as csvFile:
                            writer = csv.writer(csvFile)
                            writer.writerows(csvData)
                            firstWrite = True
                        csvFile.close()
                    else:
                        with open(filename, 'a') as csvFile:
                            writer = csv.writer(csvFile)
                            writer.writerows(csvData)
                        csvFile.close()
                    return   
        except (tweepy.TweepError, StopIteration):
            print('hit rate limit ... saved this batch to csv ... sleeping for 15 mins')
            # save data to csv and write to csv in Data/tw/
            if (not firstWrite):
                with open(filename, 'w') as csvFile:
                    writer = csv.writer(csvFile)
                    writer.writerows(csvData)
                    firstWrite = True
                csvFile.close()
            else:
                with open(filename, 'a') as csvFile:
                    writer = csv.writer(csvFile)
                    writer.writerows(csvData)
                csvFile.close()
            time.sleep(15*60)

def main():
    searchQuery = {'Basketball OR #basketball OR NBA OR #nba OR March Madness OR #marchmadness' : '../data/tw/basketball.csv', 
                'Baseball OR #baseball OR MLB OR #mlb OR Opening Day OR #openingday' : '../data/tw/baseball.csv', 
                'Hockey OR #hockey OR NHL OR #nhl OR Stanley Cup OR #stanleycup' : '../data/tw/hockey.csv', 
                'Football OR #football OR NFL OR #nfl OR NFL Draft OR #nfldraft' : '../data/tw/football.csv', 
                'Cricket OR #cricket OR IPL OR #ipl' : '../data/tw/cricket.csv'}

    # search on Twitter with Keywords, retrieve tweets
    for query,path in searchQuery.items():
        limitHandler(tweepy.Cursor(api.search, q = query, tweet_mode = 'extended', lang = 'en').items(), os.path.join(path), False)
        print("done with : " + query)


if __name__ == "__main__":
    main()