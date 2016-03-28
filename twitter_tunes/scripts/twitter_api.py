# -*- coding: utf-8 -*-
"""Twitter API Call."""
import tweepy
import os

REQUEST_TOKEN_URL = 'https://api.twitter.com/oauth/request_token'
AUTHORIZATION_URL = 'https://api.twitter.com/oauth/authorize'
ACCESS_TOKEN_URL = 'https://api.twitter.com/oauth/access_token'

consumerKey = os.environ.get('TWITTER_CONSUMERKEY')
consumerSecret = os.environ.get('TWITTER_CONSUMERSECRET')
accessToken = os.environ.get('TWITTER_ACCESSTOKEN')
accessTokenSecret = os.environ.get('TWITTER_ACCESSTOKENSECRET')

auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
auth.set_access_token(accessToken, accessTokenSecret)
api = tweepy.API(auth)

print(api.trends_place(1))
