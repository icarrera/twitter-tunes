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
    """Return a single trend from a list of trends.

    Currently Selects #1 trend.
    TODO: Select based on music relevence or some other quality.
    """
    return trends[0]


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
    trend = choose_trend(twitter_api.call_twitter_api())
    parsed_trend = parser.parse_trend(trend)
    youtube_url = youtube_api.get_link(parsed_trend)
    message = create_message(trend, youtube_url)
    make_tweet(message)
    print('@trending__tunes Made a Tweet:\n{}'.format(message))

if __name__ == '__main__':
    main()
