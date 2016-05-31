class OAuthHandler:
    def __init__(self, ckey, csecret):
        self.ckey = ckey
        self.csecret = csecret

    def set_access_token(self, akey, asecret):
        pass

class API:
    def __init__(self, auth):
        self.auth = auth
    def update_with_media(self, latest, status):
        print(latest)
        print(status)
