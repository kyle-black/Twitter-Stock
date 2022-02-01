import tweepy as tw
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import nltk
from nltk.corpus import stopwords

from textblob import Word, TextBlob
import sqlite3
import config

connection = sqlite3.connect(config.DB_FILE)
connection.row_factory = sqlite3.Row
cursor = connection.cursor()


consumer_key = 'epWw8VILVgHNQ7tatmpTuBZ4M'
Secret_key = 'W7tcsyVa1ClOiCccKnIrwxhSFoa8u4D91FqeLk9KR83Xd936EI'
access_token = '1176589291838988288-d3W3sxBTUXGmz4dusWBkGVLKP6nTPR'
Access_Token_Secret = 'f6wNlC0kN3FqVN8yQovpe4rcHPdQOPBKH8ftDu4iN78gh'

auth = tw.OAuthHandler(consumer_key, Secret_key)
auth.set_access_token(access_token, Access_Token_Secret)
api = tw.API(auth, wait_on_rate_limit=True)

hashtag = '$TSLA'
#hastag2= '$AAPL OR $MSFT OR $GOOG OR $AMZN OR $FB OR $NVDA OR $ADBE OR $CSCO OR $CRM'
#query = tw.Cursor(api.search_tweets, q=hashtag).items(1000)
# tweets = [{'Tweets': tweet.text, 'Timestamp': tweet.created_at}
#         for tweet in query]

query = tw.Cursor(api.search_tweets, q=hashtag).items(1000)
tweets = [{'Tweets': tweet.text, 'Timestamp': tweet.created_at}
          for tweet in query]

df = pd.DataFrame.from_dict(tweets)


#Apple_Refs =['Apple', 'AAPL', '$AAPL', 'Mac']

TESLA_refs = ['Tesla', 'TSLA', '$TSLA']


def identify_subject(tweet, refs):
    flag = 0
    for ref in refs:
        if tweet.find(ref) != -1:
            flag = 1
    return flag


df['Tesla'] = df['Tweets'].apply(lambda x: identify_subject(x, TESLA_refs))


nltk.download('stopwords')
nltk.download('wordnet')
stop_words = stopwords.words('english')
custom_stopwords = ['RT']


def preprocess_tweets(tweet, custom_stopwords):
    preprocessed_tweet = tweet
    preprocessed_tweet.replace('[^\w\s]', '')
    preprocessed_tweet = ' '.join(
        word for word in preprocessed_tweet.split() if word not in stop_words)
    preprocessed_tweet = ' '.join(
        word for word in preprocessed_tweet.split() if word not in custom_stopwords)
    preprocessed_tweet = ' '.join(Word(word).lemmatize()
                                  for word in preprocessed_tweet.split())
    return (preprocessed_tweet)


df['Processed Tweet'] = df['Tweets'].apply(
    lambda x: preprocess_tweets(x, custom_stopwords))


df['polarity'] = df['Processed Tweet'].apply(
    lambda x: TextBlob(x).sentiment[0])
df['subjectivity'] = df['Processed Tweet'].apply(
    lambda x: TextBlob(x).sentiment[1])


# df[df['Tesla'] == 1][['Tesla', 'polarity', 'subjectivity']].groupby(
#   'Tesla').agg([np.mean, np.max, np.min, np.median])

#Tesla = df[df['Tesla'] == 1][['Timestamp', 'polarity']]
#Tesla = Tesla.sort_values(by='Timestamp', ascending=True)
#Tesla['MA Polarity'] = Tesla.polarity.rolling(10, min_periods=10).mean()


df = df[['Timestamp', 'polarity', 'subjectivity',
         'Processed Tweet']]


df.to_sql('tesla', connection, if_exists='replace', index=False)

connection.commit()
