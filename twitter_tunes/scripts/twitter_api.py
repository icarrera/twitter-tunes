# -*- coding: utf-8 -*-
"""Twitter API Call."""
import tweepy
import os


WOEID_US = 23424977
consumerKey = os.environ.get('TWITTER_CONSUMERKEY', None)
consumerSecret = os.environ.get('TWITTER_CONSUMERSECRET', None)
accessToken = os.environ.get('TWITTER_ACCESSTOKEN', None)
accessTokenSecret = os.environ.get('TWITTER_ACCESSTOKENSECRET', None)


def get_twitter_response(api):
    """Make API call to Twitter and return response."""
    resp = api.trends_place(WOEID_US)
    return resp


def extract_twitter_trends(resp):
    """Extract trending topics from Twitter response."""
    trend_list = [trend['name'] for trend in resp[0]['trends']]
    return trend_list


def call_twitter_api():
    """Twitter API call to get trending topics."""
    if consumerKey and consumerSecret and accessToken and accessTokenSecret:
        auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
        auth.set_access_token(accessToken, accessTokenSecret)
        api = tweepy.API(auth)

        resp = get_twitter_response(api)
        trend_list = extract_twitter_trends(resp)

        return trend_list[:10]
    else:
        print('Missing OAuth key or token')
        raise ValueError('Missing OAuth key or token.')
