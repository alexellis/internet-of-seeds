import time

class Tweeter:
    def __init__(self, config, tweepy):
        self.tweepy = tweepy
        self.config = config

    ## Tweets sensor values and timestampedimage. Needs to be passed status (timestamp,
    ## and sensors values pulled from data log) and the latest image filename.
    def send(self, status, latest):

        ## Read config from config.py file, if this doesn't exist, use config.example.py
        ckey = self.config["ckey"]
        csecret = self.config["csecret"]
        akey = self.config["akey"]
        asecret = self.config["asecret"]

        auth = self.tweepy.OAuthHandler(ckey, csecret)
        auth.set_access_token(akey, asecret)
        api = self.tweepy.API(auth)
        api.update_with_media(latest, status=status)

    def get_last_line(self, log_file):
        lines = log_file.readlines()
        return lines[len(lines)-1]

    def build(self):
        ## Set the latest image filename, grab the last line from the data log.
        latest = self.config["working_directory"] + 'latest.jpg'

        l = None
        fn = self.config["working_directory"] + 'sensors.log'
        with open(fn) as log_file:
            l = self.get_last_line(log_file)

        ## Format the sensor values nicely for tweeting, run the tweet_pic function.
        sensor_vals = l.rstrip().split('\t')
        valid = False
        status = None

        if(len(sensor_vals) == 7):
            status = '%s: Temp: %s C, Press: %s hPa, Light: %s lux, RGB: %s,%s,%s.' % tuple(sensor_vals)
            valid = True

        status = time.strftime(time.ctime())
        return {"status": status, "latest": latest, "valid": valid}
