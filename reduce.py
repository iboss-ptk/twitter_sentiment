from itertools import groupby
from operator import itemgetter
import sys
import json


def get_data():
    for line in sys.stdin:
        emo, tweet_data = line.split("\t", 1)
        tweet_data = json.loads(tweet_data)
        yield [emo, tweet_data]


def main():
    data = get_data()
    for emo, group in groupby(data, itemgetter(0)):
        tweet = json.dumps([tweet_data for tweet_data in group])
        print("%s\t%s" % (emo, tweet))

if __name__ == "__main__":
    main()
