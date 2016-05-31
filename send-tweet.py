import faketweepy as tweepy

from tweeter import Tweeter
import config as config
tweeter = Tweeter(config.config, tweepy)

tweet = tweeter.build()
if(tweet["valid"]):
    tweeter.send(tweet["latest"], tweet["status"])
else:
    print("Declining to tweet because dataset or config is not valid.")
