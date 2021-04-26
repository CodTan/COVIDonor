'''
TODO file docsrting
'''
import tweepy
# from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
# from tweepy import StreamListener
from flask import Markup
from config import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET


class Tweets:
    '''
    TODO class docstring
    '''

    def __init__(self):
        # self.l = MyStreamListener()
        self.auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        self.auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
        self.api = tweepy.API(self.auth, wait_on_rate_limit=True)
        self.url = "https://twitter.com/user/status/"

    def tweet2html(self, tweet_id):
        '''
        TODO: Function DocString
        '''
        tweet_url = self.url + tweet_id
        tweet_html = self.api.get_oembed(url = tweet_url,hide_media = 1,hide_thread = 1)['html'].replace('\n','') # api.get_oembed returns an HTML object equivalent to the id. but requires processing before passing to Markup() in flask.
        # tweet_html = tweet_html.replace('"',r"\"")
        tweet_html = tweet_html.replace("'",r"\'") # escaping relevant characters
        tweet_html = tweet_html.replace('%',r"%%")
        return Markup(tweet_html)

    def fetch_tweets(self, search_query=None):
        '''
        TODO: Function DocString
        '''
        if search_query is None:
            search_query = '(((("i+am"("ready"OR"willing")"to"("donate"OR"give"))OR("i+can "("give"OR"donate"))OR("i"("want"OR"wish")"to"("give"OR"donate"))OR("i+am""available+to"("give"OR"donate")))OR("i+have+recovered""COVID"))"plasma") -filter:retweets -modi'

        # from_input: optional
        # city_name = ''
        # verified = ''

        # list of 'StatusObjects'
        returned_tweets = self.api.search(q=search_query, result_type="recent",count=10) #, include_entities=True

        tweets_html = list()

        for tweets in returned_tweets:
            tweets_html.append(self.tweet2html(tweets._json['id_str']))

        return tweets_html

    # def __repr__(self):
    #     return f"Latest tweets using {self.url}"

'''
# YEH KARNA HAI AB

# Input(textbox): city_name->(search_query + city_name)
# Input(checkbox): verified/unverified->(search_query + "verified")
# Input(button): same search_query, reload next 10 tweets
# brackets check kar balanced hain ya nahi



################################# FINAL SEARCH_QUERY ###############################
# (((("i+am"("ready"OR"willing")"to"("donate"OR"give"))OR("i+can "("give"OR"donate"))OR("i"("want"OR"wish")"to"("give"OR"donate"))OR("i+am""available+to"("give"OR"donate")))OR("i+have+recovered""COVID"))"plasma")-filter:retweets"delhi""verified"

# TRIED SEARCH QUERIES
# ("i"+(("am"+("willing"OR"ready"OR"available"))OR"want")+"to"+("donate"OR"give")+"plasma")
# (("i+am+ready+to+donate"OR"i+am+willing+to+donate"OR"i+can+give"OR"i+can+donate"OR"i+am+ready+to+give"OR"i+am+willing+to+give"OR"i+want+to+give"OR"i+want+to+donate"OR"i+am+available+to+give"OR"i+am+available+to+donate")"plasma")OR("i+have+recovered+from+covid")
# ("i"(("am"("willing"OR"ready"OR"available"))OR"want")"to"("donate"OR"give")"plasma")


# "(((
#     ("i+am"("ready"OR"willing")"to"("donate"OR"give"))OR
#     ("i+can "("give"OR"donate"))OR
#     ("i"("want"OR"wish")"to"("give"OR"donate"))OR
#     ("i+am""available+to"("give"OR"donate"))
#    )OR
#   ("i+have+recovered""COVID")
#  )
# plasma)-filter:retweets"

# (((("i+am"("ready"OR"willing")"to"("donate"OR"give"))OR("i+can "("give"OR"donate"))OR("i"("want"OR"wish")"to"("give"OR"donate"))OR("i+am""available+to"("give"OR"donate")))OR("i+have+recovered""COVID"))plasma)-filter:retweets

# ((("i+am+ready+to+donate"OR"i+am+willing+to+donate"OR"i+can+give"OR"i+can+donate"OR"i+am+ready+to+give"OR"i+am+willing+to+give"OR"i+want+to+give"OR"i+want+to+donate"OR"i+am+available+to+give"OR"i+am+available+to+donate")OR("i+have+recovered""COVID"))"plasma")-filter:retweets
'''