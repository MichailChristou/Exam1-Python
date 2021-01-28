from tweepy import API, Cursor, Stream, OAuthHandler
from tweepy.streaming import StreamListener
import pandas as pd
import re

access_token = "1081576257614241793-2qcblON924ywtOHJe02I6fFrX7oSxw"
access_token_secret = "GUecr8JN6vQBC1X6GTXSBpUVUh1Du9F7ctblhdKyHJ9R2"
consumer_key = "8AJZTXk9rJLkt5eSJeGdlnG8Z"
consumer_secret = "Yx5DO3wAAMq6lYvLZr8cgoFfz8eIME2rFzjGVRNV25k20g6Yqc"

class TwitterClient():
    def __init__(self, twitter_user=None):
        self.auth = TwitterAuthenticator().authenticate_twitter_app()
        self.twitter_client = API(self.auth)

        self.twitter_user = twitter_user

    def get_twitter_client_api(self):
            return self.twitter_client

    def get_user_timeline_tweets(self, num_tweets):
        tweets = []
        for tweet in Cursor(self.twitter_client.user_timeline, id=self.twitter_user).items(num_tweets):
            tweets.append(tweet)
        return tweets


class TwitterAuthenticator():

    def authenticate_twitter_app(self):
        auth = OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        return auth


class TwitterStreamer():

    def __init__(self):
        self.twitter_autenticator = TwitterAuthenticator()

    def stream_tweets(self, fetched_tweets_filename, hash_tag_list):

        listener = TwitterListener(fetched_tweets_filename)
        auth = self.twitter_autenticator.authenticate_twitter_app()
        stream = Stream(auth, listener)

        stream.filter(track=hash_tag_list)


class TwitterListener(StreamListener):

    def __init__(self, fetched_tweets_filename):
        self.fetched_tweets_filename = fetched_tweets_filename

    def on_data(self, data):
        try:
            print(data)
            with open(self.fetched_tweets_filename, 'a') as tf:
                tf.write(data)
            return True
        except BaseException as e:
            print("Error on_data %s" % str(e))
        return True


def convert(newdata):
    return ([i for item in newdata for i in item.split()])

twitter_client = TwitterClient()
api = twitter_client.get_twitter_client_api()
twitusername = input("Δωσε ενα ονομα χρηστη Twitter: ")

tweets = api.user_timeline(screen_name=twitusername, count=10)

df = pd.DataFrame(data=[tweet.text for tweet in tweets], columns=['Tweets'])
df['cleanTweets'] = df["Tweets"].apply(lambda x: ''.join([" " if ord(i) < 32 or ord(i) > 126 else i for i in x]))
df['cleanTweetsfromtrash'] = df['cleanTweets'].apply(lambda x: re.split('https:\/\/.*', str(x))[0])

newdata = df['cleanTweetsfromtrash'].tolist()
lastnewdata = (convert(newdata))
sortnewdata = sorted(lastnewdata, key=len)

print("Οι μικροτερες λεξεις που χρησιμοποιηθηκαν στα τελευταια 10 tweets του χρηστη @"+twitusername+" ειναι: "+sortnewdata[0],sortnewdata[1],sortnewdata[2],sortnewdata[3],sortnewdata[4])
print("Οι μεγαλυτερες λεξεις που χρησιμοποιηθηκαν στα τελευταια 10 tweets του χρηστη @"+twitusername+" ειναι: "+sortnewdata[-1],sortnewdata[-2],sortnewdata[-3],sortnewdata[-4],sortnewdata[-5])