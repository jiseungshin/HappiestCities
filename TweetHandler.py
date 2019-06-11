import tweepy


class StreamListener(tweepy.StreamListener):
    """ Tweepy Streaming object to connect to Twitter's stream of Tweets"""
    def on_status(self, status):
        print(status.text)

class TweetHandler:
    """ TweetHandler contains various useful methods for dealing with Tweets. Some
    methods include streaming Tweets and searching Tweets. Public methods also
    exist to create Tweet objects from these Tweet "mining" tools.
    """

    def __init__(self, consumer_key, consumer_secret,
                 access_token, access_token_secret):
        """
        Initialize TweetHandler with API information
        :param consumer_key:
        :param consumer_secret:
        :param access_token:
        :param access_token_secret:
        """
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)

        self.api = tweepy.API(auth)
        self.streamListener = StreamListener()


    def streamTwitter(self):

        stream = tweepy.Stream(auth=self.api.auth, listener=self.streamListener)
        print(stream)









