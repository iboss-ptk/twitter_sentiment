import plotly.plotly as py
from plotly.graph_objs import *
import sys
import json


def get_data():
    for line in sys.stdin:
        emo, tweet_list = line.split("\t", 1)
        tweet_list = json.loads(tweet_list)
        yield tweet_list


def main():
    data = get_data()
    score_freq = dict()
    for tweet_list in data:
        for emo, tweet in tweet_list:
            s = int(tweet['score'])
            if s not in score_freq:
                score_freq[s] = 1
            else:
                score_freq[s] += 1
    min_score = min(score_freq)
    max_score = max(score_freq)
    score_band = list(range(min_score, max_score+1))
    trace = Bar(
        x=score_band,
        y=[score_freq[sb] for sb in score_band]
    )
    data = Data([trace])
    plot_url = py.plot(data, filename="grand-hyatt-histogram")
    print(plot_url)


if __name__ == "__main__":
    main()
