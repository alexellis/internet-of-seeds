#!/usr/bin/python

#import faketweepy as tweepy
import tweepy
from logreader import LogReader

from tweeter import Tweeter
import config as config
tweeter = Tweeter(config.config, tweepy)
log_reader = LogReader(config.config)

tweet = tweeter.build()
if(tweet["valid"]):
    print(tweet)
    print("Uploading "+ tweet["latest"])
    sensor_data = log_reader.read()

    tweeter.send(sensor_data, tweet["latest"])
else:
    print("Declining to tweet because dataset or config is not valid.")
