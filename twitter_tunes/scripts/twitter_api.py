# -*- coding: utf-8 -*-
"""Twitter API Call."""
import tweepy
import os


WOEID_US = 23424977
consumerKey = os.environ.get('TWITTER_CONSUMERKEY')
consumerSecret = os.environ.get('TWITTER_CONSUMERSECRET')
accessToken = os.environ.get('TWITTER_ACCESSTOKEN')
accessTokenSecret = os.environ.get('TWITTER_ACCESSTOKENSECRET')

auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
auth.set_access_token(accessToken, accessTokenSecret)
api = tweepy.API(auth)

resp = api.trends_place(WOEID_US)
# print(u'response:', resp)

trend_list = [trend['name'] for trend in resp[0]['trends']]
print(u'\ntrend_list:\n', trend_list)
