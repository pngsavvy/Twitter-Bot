# This bot moniters Twitter mentions and automatically replies

import tweepy

CONSUMER_KEY = "" # enter customer key
CONSUMER_SECRET = "" # enter customer secret
ACCESS_KEY = "" # enter access key
ACCESS_SECRET = "" # enter access secret

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY,ACCESS_SECRET)
api = tweepy.API(auth)

# checks for when account is mentioned
mentions = api.mentions_timeline()

api.update_status("I am updating my twitter status")

for mention in mentions:
    print(str(mention.id) + '-' + mention.text)
    if '#hello' in mention.text.lower():
        print("found hello")
        api.update_status("hello back to you", mention.id)
