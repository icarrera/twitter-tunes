# -*- coding: utf-8 -*-
import twitter_api
import youtube_api

BASE_MESSAGE = u"""{trend} is trending right now. Here's its tune! {url}"""


def create_message(parsed_trend, youtube_url):
    """Return a message the bot will post."""
    return BASE_MESSAGE.format(trend=parsed_trend, url=youtube_url)
