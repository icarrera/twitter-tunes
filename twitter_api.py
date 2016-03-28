# -*- coding: utf-8 -*-
"""Twitter API Call"""
import tweepy
import os

consumerKey = os.environ.get('TWITTER_CONSUMERKEY')
consumerSecret = os.environ.get('TWITTER_CONSUMERSECRET')
accessToken = os.environ.get('TWITTER_ACCESSTOKEN')
accessTokenSecret = os.environ.get('TWITTER_ACCESSTOKENSECRET')

auth = tweepy.OAuthHanler(consumerKey, consumerSecret)
auth.set_access_token(accessToken, accessTokenSecret)
api = tweepy.API(auth)

print(api.trends_place(1))
