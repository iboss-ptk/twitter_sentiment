import tweepy
import json

consumer_key = "bljICegdyVXA1QJtKoof1QHU0"
consumer_secret = "uQWawzkFnGEGX3GrPgdRnaLhYLuBM5ShSZjEj8so1oMGGNr8MU"
access_token = "137550210-jRDXkxL3kflcj8Tjdx2gtUYlz7moES6lcXYqqvvf"
access_token_secret = "C5mPoCD2lWGj6YSXq02QQnrju1K7NRZZa0tChgoyeODsu"


def twitter_search(api, max_tweets):
    tweets = tweepy.Cursor(
        api.search,
        q='four seasons hotel',
        # TODO: four seasons hotel, grand hyatt, marriott hotel
        lang='en'
    ).items(max_tweets)

    tweets = [status._json for status in tweets]
    hotel = open("four_seasons2.txt", "a+")
    for t in tweets:
        t = json.dumps(t, ensure_ascii=False)
        hotel.write(t)
        hotel.write("\n")
    hotel.close()


if __name__ == '__main__':
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth)

    twitter_search(api, 1700)
