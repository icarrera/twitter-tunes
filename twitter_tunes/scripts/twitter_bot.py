# -*- coding: utf-8 -*-
from twitter_tunes.scripts import twitter_api
import tweepy
from twitter_tunes.scripts import youtube_api
from twitter_tunes.scripts import parser
import os

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

    Will select a trend which has music relevence.
    """
    for trend in trends:
        url, is_music = youtube_api.get_link(parser.parse_trend(trend))
        if is_music:
            # if trend not in redis.recent_tweets
                # if len(redis.recent_tweets) > 5
                    # pop redis.recent[0]
                    # append trend on redis.recent
                    # You need to remake the redis object for this
                    # return trend, url
            return trend, url


def make_tweet(message):
    """Update Twitter status with message."""
    if consumerKey and consumerSecret and accessToken and accessTokenSecret:
        auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
        auth.set_access_token(accessToken, accessTokenSecret)
        api = tweepy.API(auth)
        return api.update_status(message)
    else:
        print('Missing OAuth key or token')
        raise ValueError('Missing OAuth key or token.')


def main():
    """Post a tweet about number one trend and a youtube video related to it.

    """
    try:
        trend, youtube_url = choose_trend(twitter_api.call_twitter_api())
        message = create_message(trend, youtube_url)
        make_tweet(message)
        print(u'@trending__tunes Made a Tweet:\n{}'.format(message))
    except (youtube_api.HttpError, ValueError, tweepy.TweepError):
        print(u'Something went horribly wrong.')

if __name__ == '__main__':
    main()
