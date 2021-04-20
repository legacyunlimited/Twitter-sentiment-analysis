import csv
from textblob import TextBlob
import re
import pandas as pd
import twint
import nest_asyncio

# For loop already running runtime error
nest_asyncio.apply()


def clean_tweet(tweet):
    ''' 
    Utility function to clean tweet text by removing links, special characters 
    using simple regex statements. 
    '''
    return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())


def get_tweet_sentiment(tweet):
    '''
    Utility function to classify sentiment of passed tweet 
    using textblob's sentiment method 
    '''
    # create TextBlob object of passed tweet text
    analysis = TextBlob(tweet)
    # set sentiment
    if analysis.sentiment.polarity > 0:
        return 'positive'
    elif analysis.sentiment.polarity == 0:
        return 'neutral'
    else:
        return 'negative'


def analyse_tweet(tweet):
    '''
    Utility function to create a dictionary with the tweet's 
    cleaned text and sentiment. 
    '''
    tweet_dict = {}
    cleaned_tweet = clean_tweet(tweet)
    tweet_dict['text'] = cleaned_tweet
    tweet_dict['sentiment'] = get_tweet_sentiment(cleaned_tweet)
    return tweet_dict


print("This program will get the latest 100 tweets according to the topic you input and generate a sentiment.csv file after performing sentiment analysis on each tweet.")
search_topic = input("\nEnter the topic you need the tweets about: ")

# configuration
config = twint.Config()
config.Search = search_topic
config.Lang = "en"
config.Limit = 100
config.Store_csv = True
config.Output = "tweets.csv"


# running search
twint.run.Search(config)

try:
    df = pd.read_csv('tweets.csv')
except:
    print("tweets.csv does not exist")
else:
    with open('sentiments.csv', 'w', newline='', encoding='UTF-8') as file:
        writer = csv.writer(file)
        writer.writerow(['tweet', 'sentiment'])
        for tweet in df['tweet']:
            temp_list = []
            tweet_sentiment = analyse_tweet(tweet)
            temp_list.append(tweet)
            temp_list.append(tweet_sentiment['sentiment'])
            writer.writerow(temp_list)
    file.close()

print("You can now check the file sentiments.csv to check the sentiment analysis of the tweets.")
