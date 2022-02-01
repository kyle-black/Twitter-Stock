import tweepy
import keys
import random
import json
import sqlite3
import config
import DateTime
from datetime import datetime

import pandas as pd

connection = sqlite3.connect(config.DB_FILE)
connection.row_factory = sqlite3.Row
cursor = connection.cursor()


Api_key = keys.Api_key
Api_Key_Secret = keys.Api_Key_Secret
Bearer_Token = keys.Bearer_Token
Access_Token = keys.Access_Token
Access_Token_Secret = keys.Access_Token_Secret


# authentioacaton
def getClient():
    client = tweepy.Client(bearer_token=Bearer_Token,
                           consumer_key=Api_key,
                           consumer_secret=Api_Key_Secret,
                           access_token=Access_Token,
                           access_token_secret=Access_Token_Secret)

    return client


def searchTweets(query):
    client = getClient()

   # tweets = client.search_recent_tweets(
    #   query=query, tweet_fields=['context_annotations', 'created_at'], expansions='author_id', max_results=100)

    tweets = client.search_recent_tweets(
        query=query, max_results=100)
    tweet_data = tweets.data
    results = []

    if not tweet_data is None and len(tweet_data) > 0:
        for tweet in tweet_data:
            #obj = {}

            #obj['id'] = tweet.id
            #obj['text'] = tweet.text
            #obj['user'] = tweet.author_id
            #obj['time'] = tweet.created_at

            results.append(tweet.text)
    else:
        return []

    return results


# pennylist = ['IMPP', 'GODYF', 'DKGR', 'SHIP', 'FLDM', 'SKYI', 'IQST', 'SXTC', 'MWWC', 'VCNX', 'INVZ', 'OTLK', 'CZOO', 'XELA', 'AMRN', 'AGRX', 'AMWL', 'EQLB', 'TPTW', 'UGP', 'BBD',
 #            'MONI', 'GOED', 'SDC', 'MNMD', 'ESPR', 'GSAT', 'IGEX', 'ASTI', 'EWLL', 'RGBP', 'VNUE', 'SCNA', 'PROG', 'CKPT', 'AIAD', 'OQUV', 'DUTV', 'PTPI', 'GNCP', 'SNMP', 'INTV', 'LTNC', 'SBEV']


# for stock in pennylist:
#    cursor.execute("""
 #           SELECT symbol, name FROM stock""")
#rows = cursor.fetchall()

# print(rows)
#stock_dict = {}
#symbols = [(row['symbol']) for row in rows]

# for row in rows:
#    stock_dict[row['symbol']] = row['name']

# print(stock_dict)
# for stock in pennylist:
#    try:
 #       d = stock_dict[stock]
 #   except Exception as e:
 #       print(f'did not find{stock}')
# print(d)
insurance_companies = ['State Farm', 'Geico', 'Progressive Insurance', 'Allstate', 'USAA', 'Liberty Insurance',
                       'Farmers Insurance', 'Nationwide Insurance', 'Travelers Insurance', 'American Family Insurance']

car_companies = ['Ford', 'Tesla', 'Chevy', 'Toyota',
                 'Honda', 'Hyundai', 'Volswagen', 'Kia']
# query = ' State Farm OR Geico OR Progressive Insurance OR Allstate OR USAA OR Liberty Insurance OR Farmers Insurance OR Nationwide Insurance OR Travelers Insurance OR American Family Insurance lang:en -is:retweet'
#word_search = ['hat', 'cow', 'orange', 'hammer', 'clock']

company_dict = {}

for idx, name in enumerate(car_companies):
    i = searchTweets(f'{name} lang:en')

    company_dict[name] = str(i)

'''
now = datetime.now()
id = 1
formatted_date = now.strftime('%Y-%m-%d %H:%M:%S')


for key, value in company_dict.items():
    #time = DateTime('now')
    cursor.execute("INSERT INTO cars (name,tweets) VALUES (?, ?)",
                   (key, value))

'''

df = pd.DataFrame(company_dict.items(), columns=['name', 'tweets'])

df.to_sql('car_tweet', connection, if_exists='append', index=False)

connection.commit()


#df.to_sql('car_tweet', connection, if_exists='replace', index=False)

#now = datetime.now()
#df['time'] = str(now)

# print(df)


#df.to_sql('car_tweet', connection, if_exists='replace', index=False)

# connection.commit()
print(company_dict)

# connection.commit()
# print(company_dict['Honda'])
#tweets = searchTweets('hats')


# cursor.execute("INSERT INTO cars (id, name, dt, tweets) VALUES (?, ?, ?, ?)",
#                  (idx, name, DateTime('now'), i))
'''
'''
'''
if len(tweets) > 0:
    for x in tweets:
        print(x)
    else:
        print('No Matching tweeets found')
'''
