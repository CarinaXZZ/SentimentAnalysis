from pymongo import MongoClient
import json
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import datetime

# The MongoDB connection info.
# Database name: TwitterStream
# Collection name: is tweets.

# client = MongoClient('mongodb://myUserAdmin:abc123@localhost:27017/TwitterStream')
client = MongoClient('localhost', 27017)
db = client.WorldCupData # database: WorldCupData
collection = db.tweets # collection: tweets


# The keywords and language to be tracked.
keywords = ['#FIFA', '#WorldCup']
language = ['en']

# Twitter App Authentication .
consumer_key = "d6EaJsmmsZt1T5Vpiykj5g4Ph"
consumer_secret = "IwVI4iISvtPH1qj8gmivdoGLakyCGtnnbcgUM6fugCrSREn1J4"
access_token = "832567188057968641-icpqjBUt6SdIlyRlhHLXkiFQRm1as6o"
access_token_secret = "BPSDnvcojwzjJFE60PUp2MdldJ4RJ3RcOTMORyMEMnKI4"


class MyListener(StreamListener):
    '''
      This is a stream listener that used to get the Tweets from stream by keywords and language
      The id, username, text, hashtags, and the timestamp of the tweets will be stored in MongoDB
    '''

    def on_data(self, data):

        tweet = json.loads(data)
        tweet_id = tweet['id_str']  # The Tweet ID from Twitter in string format
        username = tweet['user']['screen_name']  # The username of the Tweet author
        text = tweet['text']  # text of the Tweet
        hashtags = tweet['entities']['hashtags']  # hashtags in the Tweet
        dt = tweet['created_at']  # The timestamp of when the Tweet was created
        date = datetime.datetime.strptime(dt, '%a %b %d %H:%M:%S +0000 %Y')

        tweet_db = {'id':tweet_id, 'username':username, 'text':text, 'hashtags':hashtags, 'date':date}
        # print tweet_db
        collection.save(tweet_db)

        print username + ': ' + text

        return True

    # Report the error
    def on_error(self, status):
        print status


if __name__ == '__main__':
    #authentication for Twitter API
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, MyListener())
    stream.filter(track=keywords, languages=language)

