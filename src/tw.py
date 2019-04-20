import tweepy
import csv
import os.path
import time
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize 
from nltk.stem import PorterStemmer 
import string
import re

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

def gatherTweet(pathin, pathout):    
    with open(os.path.join(pathin)) as csvTweet:  
        reader = csv.DictReader(csvTweet)
        with open(os.path.join(pathout), 'w') as tweetTxt:
            for tweet in reader:
                tweetTxt.write(tweet['Text'].replace('\n', "") + '\n')
            tweetTxt.close()
    csvTweet.close()

def cleanup(unclean, clean):
    count = 1
    stop_words = set(stopwords.words('english'))
    with open(os.path.join(unclean)) as uncleanTweet:
        for line in uncleanTweet:
            wordsToWrite = []
            words = word_tokenize(line)
            for word in words:
                if not word in stop_words:
                    if not (any(i.isdigit() for i in (word.split()[0]))):
                        word = re.sub(r'[^\w\s]','', word)
                        word = word.lower()       
                        wordsToWrite.append(word)
            with open(os.path.join(clean), 'a') as cleanTweet:
                for cleanWord in wordsToWrite:
                    cleanTweet.write(cleanWord + " ")
            cleanTweet.close()
            if (count % 1000 == 0):
                print ('cleaned %d lines' % count)
            count += 1            
    uncleanTweet.close()
    print("\n\n\n ============ DONE COLLECTING " + clean + " ============\n\n\n")

def main():
    
    searchQuery = {
                'Basketball OR #basketball OR NBA OR #nba OR March Madness OR #marchmadness' : '../data/tw/tweet_csv/basketball.csv', 
                'Baseball OR #baseball OR MLB OR #mlb OR Opening Day OR #openingday' : '../data/tw/tweet_csv/baseball.csv', 
                'Hockey OR #hockey OR NHL OR #nhl OR Stanley Cup OR #stanleycup' : '../data/tw/tweet_csv/hockey.csv', 
                'Football OR #football OR NFL OR #nfl OR NFL Draft OR #nfldraft' : '../data/tw/tweet_csv/football.csv', 
                'Cricket OR #cricket OR IPL OR #ipl' : '../data/tw/tweet_csv/cricket.csv'
                }
                    
    # search on Twitter with Keywords above, retrieve tweets
    for query,path in searchQuery.items():
        limitHandler(tweepy.Cursor(api.search, q = query, tweet_mode = 'extended', lang = 'en').items(), os.path.join(path), False)
        print("done with : " + query)
    
    allPaths = {'../data/tw/basketTweet.txt' : '../data/tw/tweet_csv/basketball.csv', 
                '../data/tw/baseTweet.txt': '../data/tw/tweet_csv/baseball.csv', 
                '../data/tw/hockeyTweet.txt' : '../data/tw/tweet_csv/hockey.csv', 
                '../data/tw/footTweet.txt' : '../data/tw/tweet_csv/football.csv', 
                '../data/tw/cricTweet.txt' : '../data/tw/tweet_csv/cricket.csv'}

    # save all the tweets as a txt
    for txtFile,csvFile in allPaths.items():
        gatherTweet(csvFile, txtFile)

    cleaned = {
        '../data/tw/tweet_text/basketTweet.txt' : '../data/tw/clean_tweets/basketball.txt', 
        '../data/tw/tweet_text/baseTweet.txt': '../data/tw/clean_tweets/baseball.txt', 
        '../data/tw/tweet_text/hockeyTweet.txt' : '../data/tw/clean_tweets/hockey.txt', 
        '../data/tw/tweet_text/footTweet.txt' : '../data/tw/clean_tweets/football.txt', 
        '../data/tw/tweet_text/cricTweet.txt' : '../data/tw/clean_tweets/cricket.txt'}
    
    # clean up all the tweets
    for unclean, clean in cleaned.items():
        cleanup(unclean, clean)
    
if __name__ == "__main__":
    main()