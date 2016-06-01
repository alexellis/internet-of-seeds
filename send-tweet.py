#!/usr/bin/python

#import faketweepy as tweepy
import tweepy

from tweeter import Tweeter
import config as config
tweeter = Tweeter(config.config, tweepy)

tweet = tweeter.build()
if(tweet["valid"]):
    print(tweet)
    print("Uploading "+ tweet["latest"])

    tweeter.send(tweet["status"], tweet["latest"])
else:
    print("Declining to tweet because dataset or config is not valid.")
