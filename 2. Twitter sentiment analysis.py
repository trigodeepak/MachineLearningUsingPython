import tweepy
from textblob import TextBlob
import unicodedata
import csv

#Enter key to run
consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''


auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('Trump')

f = open('twitter_sentiment_analysis.csv','w')
f.write('Tweet , Sentiment\n')


for tweet in public_tweets:
    print (tweet.text)
    analysis = TextBlob(tweet.text)
    print (analysis.sentiment)
    a = unicodedata.normalize('NFKD', tweet.text).encode('ascii','ignore')
    a = a.replace('\n', ' ')
    a = a.replace(',',' ')
    f.write(str(a)+','+str(analysis.sentiment).replace(',',' ')+'\n')
    
f.close()
    
    
