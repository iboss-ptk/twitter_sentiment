import sys
import re
import json


class Emotion:
    Positive, Neutral, Negative = range(-1, 2)


def is_en(s):
    try:
        s.encode('ascii')
    except UnicodeEncodeError:
        return False
    else:
        return True


def get_lex():
    neg = open(
        "opinion-lexicon/negative-words.txt", "r", encoding="ISO-8859-1")
    pos = open(
        "opinion-lexicon/positive-words.txt", "r", encoding="ISO-8859-1")
    neg_list = [word.strip() for word in neg.readlines()
                if not re.search(r";", word)]
    pos_list = [word.strip() for word in pos.readlines()
                if not re.search(r";", word)]
    wdict = {
        'neg': dict((e, 1) for e in neg_list),
        'pos': dict((e, 1) for e in pos_list)
    }
    neg.close
    pos.close
    return wdict


def emotion(word_list, wd):
    neg_score = len(list(filter(lambda x: x in wd['neg'], word_list)))
    pos_score = len(list(filter(lambda x: x in wd['pos'], word_list)))
    score = pos_score - neg_score
    # positive emotion
    if score >= 2:
        return (Emotion.Positive, score)
    # negative emotion
    if score <= -2:
        return (Emotion.Negative, score)
    # neutral
    return (Emotion.Neutral, score)


def word_list(text):
    text = text.split()
    wlist = [re.sub('[\W\d]', '', w).lower() for w in text if is_en(w)]
    wlist = list(filter(lambda x: x, wlist))  # no empty string
    return wlist


def get_data():
    for line in sys.stdin:
        yield json.loads(line)


def main():
    tweets = get_data()
    word_dict = get_lex()
    for tweet in tweets:
        emo = emotion(word_list(tweet['text']), word_dict)  # key
        data = json.dumps(
            {'text': tweet['text'], 'geo': tweet['geo'], 'score': emo[1]}
        )
        print("%d\t%s" % (emo[0], data))


if __name__ == "__main__":
    main()
