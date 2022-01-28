import tweepy
import keys
import random
import json

Api_key = keys.Api_key
Api_Key_Secret = keys.Api_Key_Secret
Bearer_Token = keys.Bearer_Token
Access_Token = keys.Access_Token
Access_Token_Secret = keys.Access_Token_Secret


# authentioacaton
def getClient():
    client = tweepy.Client(bearer_token=Bearer_Token, consumer_key=Api_key, consumer_secret=Api_Key_Secret,
                           access_token=Access_Token.Api_Key_Secret, access_token_secret=Access_Token_Secret)

    return client


def searchTweets(query):
    client = getClient()

    tweets = client.search_recent_tweets(query=query, max_results=10)
    tweet_data = tweets.data
    results = []

    if not tweet_data is None and len(tweet_data) > 0:
        for tweet in tweet_data:
            obj = {}
            obj['id'] = tweet.id
            obj['text'] = tweet.text
            results.append(obj)
    else:
        return []

    return results


tweets = searchTweets('crm software reccomendations')

if len(tweets) > 0:
    for x in tweets:
        print(x)
    else:
        print('No Matching tweeets found')
