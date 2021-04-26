'''
app.py
'''
import itertools
from flask import Flask, render_template, request, redirect
from tweet import Tweets

app = Flask(__name__, template_folder='templates')

# headings = ("one","two",)

# ten_tweets = ()

# for i in (0, len(tweets_HTML), 2):
#     try:
#         ten_tweets += (tweets_HTML[i], tweets_HTML[i+1])
#     except:
#         ten_tweets += (tweets_HTML[i],)


@app.route('/', methods=["POST", "GET"])
def home():
    '''
    TODO
    '''
    # html = fetch_tweets()
    # return 'Welcome!'

    if request.method == "POST":
        city_name = request.form["city"]
        search_query = '(((("i+am"("ready"OR"willing")"to"("donate"OR"give"))OR("i+can "("give"OR"donate"))OR("i"("want"OR"wish")"to"("give"OR"donate"))OR("i+am""available+to"("give"OR"donate")))OR("i+have+recovered""COVID"))"plasma") -filter:retweets -modi'
        search_query_city = search_query + " " + city_name
        tweets = Tweets()
        ten_tweets = tuple()
        tweets_html = list()

        try:
            tweets_html = tweets.fetch_tweets(search_query_city)
            ten_tweets = tuple(itertools.zip_longest(tweets_html[0::2], tweets_html[1::2],fillvalue=''))
            if len(tweets_html) == 0:
                return render_template("home.html")
            else:               
                return render_template("home.html", data=ten_tweets)
        except Exception as err: 
            return "It's not you it's me!"
        # return "This is the city query platform."


    else:

        ten_tweets = tuple()
        tweets_html = list()
        search_query = '(((("i+am"("ready"OR"willing")"to"("donate"OR"give"))OR("i+can "("give"OR"donate"))OR("i"("want"OR"wish")"to"("give"OR"donate"))OR("i+am""available+to"("give"OR"donate")))OR("i+have+recovered""COVID"))"plasma") -filter:retweets -modi'
        tweets = Tweets()
        tweets_html = tweets.fetch_tweets(search_query)

        ten_tweets = tuple(itertools.zip_longest(tweets_html[0::2], tweets_html[1::2]))

        return render_template("home.html", data=ten_tweets)
    # return render_template('home.html')

# if __name__ == "__main__":
#     app.run(debug=True)
