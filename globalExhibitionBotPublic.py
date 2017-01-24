#!/usr/bin/env python3
import tweepy
import time
import sys
import markovify
import datetime
from webScraping import getMenu


class TwitterAPI:
    def __init__(self):
        consumer_key = 
        consumer_secret = 
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        access_token = 
        access_token_secret = 
        auth.set_access_token(access_token, access_token_secret)
        self.api = tweepy.API(auth)

    def tweet(self, message):
        self.api.update_status(status=message)
if __name__ == "__main__":
    twitter = TwitterAPI()
    #twitter.tweet("testing")
    date = datetime.datetime.today().weekday()
    newTweet = getMenu(date)

    print(newTweet)
    #twitter.tweet("Today \U0001F44F  at the Global Exhibition section at Stevie \U0001F44F  the menu is: " + newTweet)
