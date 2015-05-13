from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json

consumer_key = "bljICegdyVXA1QJtKoof1QHU0"
consumer_secret = "uQWawzkFnGEGX3GrPgdRnaLhYLuBM5ShSZjEj8so1oMGGNr8MU"
access_token = "137550210-jRDXkxL3kflcj8Tjdx2gtUYlz7moES6lcXYqqvvf"
access_token_secret = "C5mPoCD2lWGj6YSXq02QQnrju1K7NRZZa0tChgoyeODsu"


class FileListener(StreamListener):
    """ A listener handles tweets are the received from the stream.
    This appends the tweets to a File named hotel
    """

    def on_data(self, data):
        hotel = open("hotel-op-stream.txt", "a+")
        hotel.write(data)
        hotel.close()
        dict_data = json.loads(data)
        print(dict_data['text'])
        return True

    def on_error(self, status):
        print(status)


if __name__ == '__main__':
    listener = FileListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    stream = Stream(auth, listener)
    stream.filter(track=["sheraton"], languages=["en"])
