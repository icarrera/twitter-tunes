# -*- coding: utf-8 -*-
from twitter_tunes.scripts import twitter_api, youtube_api, parser, redis_data
import tweepy
import os
from requests.exceptions import ConnectionError

BASE_MESSAGE = u"""{trend} is trending right now. Here's its tune! {url}"""
consumerKey = os.environ.get('TWITTER_CONSUMERKEY', None)
consumerSecret = os.environ.get('TWITTER_CONSUMERSECRET', None)
accessToken = os.environ.get('TWITTER_ACCESSTOKEN', None)
accessTokenSecret = os.environ.get('TWITTER_ACCESSTOKENSECRET', None)


def create_message(parsed_trend, youtube_url):
    """Return a message the bot will post."""
    return BASE_MESSAGE.format(trend=parsed_trend, url=youtube_url)


def choose_trend(trends):
    """Return a single trend and its yt url from a list of trends.

    Will select a trend which has music relevence and
    has not been posted recently.
    """
    for trend in trends:
        url, is_music = youtube_api.get_link(parser.parse_trend(trend))
        last_tweets = redis_data.get_redis_data(u'last_tweets')
        if last_tweets == {}:
            last_tweets = []
        if is_music:
            if trend not in last_tweets:
                if len(last_tweets) >= 5:
                    last_tweets = last_tweets[1:]
                last_tweets.append(trend)
                redis_data.set_redis_data(u'last_tweets', last_tweets)
                return trend, url


def make_tweet(message):
    """Update Twitter status with message."""
    if consumerKey and consumerSecret and accessToken and accessTokenSecret:
        auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
        auth.set_access_token(accessToken, accessTokenSecret)
        api = tweepy.API(auth)
        return api.update_status(message)
    else:
        raise ValueError('Missing OAuth key or token.')


def main():
    """Post a relevant video with music for a trend."""
    try:
        # Get a list of trends from the redis DB
        try:
            current_trends = redis_data.get_redis_data(u'trends')[u'trends']
        except KeyError:  # There's some key issue on redis
            # Just use real twitter
            print('Key Error present. Using real twitter.')
            trend, youtube_url = choose_trend(twitter_api.call_twitter_api())
        else:
            trend, youtube_url = choose_trend(current_trends)
        message = create_message(trend, youtube_url)
        make_tweet(message)
        print(u'@trending__tunes Made a Tweet:\n{}'.format(message))
    except (youtube_api.HttpError, ValueError,
            tweepy.TweepError, ConnectionError, TypeError):
            print(u'Something went horribly wrong.')
            return u'Something went horribly wrong.'

if __name__ == '__main__':
    main()
