import json
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import StreamListener
import config

class MyStreamListener(StreamListener):
	def on_data(self,data):
		global_dict.append(json.loads(data))
		return True
	def on_error(self,status_code):
		if status_code == 420:
			return False

if __name__=='__main__':
	l = MyStreamListener()
	auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
	auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
	global_dict = list()

	stream = Stream(l, auth, tweet_mode='extended_tweet')
	stream.filter(track=['i can donate plasma','i want to donate plasma','i am willing to donate plasma'])