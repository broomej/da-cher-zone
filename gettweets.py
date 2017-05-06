import tweepy
import random
import credentials
# stores the authentication credentials as ckey, csecret, at, atsecret
# credentials.py is ignored by git

auth = tweepy.OAuthHandler(credentials.ckey, credentials.csecret)
auth.set_access_token(credentials.at, credentials.atsecret)
api = tweepy.API(auth)

cher_tweets = api.user_timeline(124003770, count=10)

tweet_lib = []

for tweet in cher_tweets:
	if not hasattr(tweet, 'retweeted_status') and not \
	tweet.text.startswith("RT @") and not \
	tweet.text.startswith("@"):
		tweet_lib.append(tweet.text.encode("UTF-8"))

tweet = random.choice(tweet_lib)

# I may want to revisit this section to make sure I don't pick the same tweet twice