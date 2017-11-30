# Dependencies
# import json
import time
import tweepy
import apikeys

# Twitter API Keys
consumer_key = apikeys.D_TWITTER_CONSUMER_KEY
consumer_secret = apikeys.D_TWITTER_CONSUMER_SECRET
access_token = apikeys.D_TWITTER_ACCESS_TOKEN
access_token_secret = apikeys.D_TWITTER_ACCESS_TOKEN_SECRET

# Twitter credentials
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())


# Create a function that tweets
def TweetOut(tweet_number):
    status = ("Can't stop. Won't stop. Chatting! "
              f"This is Tweet #{tweet_number}!")
    # api.update_status(status)
    print(status)


# Create a function that calls the TweetOut function every minute
counter = 0

# Infinitely loop
while True:

    # Call the TweetQuotes function and specify the tweet number
    TweetOut(counter)

    # Once tweeted, wait 60 seconds before doing anything else
    time.sleep(60)

    # Add 1 to the counter prior to re-running the loop
    counter = counter + 1
