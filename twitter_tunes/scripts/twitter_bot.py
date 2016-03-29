# -*- coding: utf-8 -*-
import twitter_api
import youtube_api
import parser
import sys

BASE_MESSAGE = u"""{trend} is trending right now. Here's its tune! {url}"""


def create_message(parsed_trend, youtube_url):
    """Return a message the bot will post."""
    return BASE_MESSAGE.format(trend=parsed_trend, url=youtube_url)


def choose_trend(trends):
    """Return a single trend from a list of trends.

    Currently Selects #1 trend.
    TODO: Select based on music relevence or some other quality.
    """
    return trends[0]

if __name__ == '__main__':
    trend = '#ThingsIWantSiriToSay'
    url = youtube_api.generate_youtube_link(
            youtube_api.youtube_parse(
                youtube_api.youtube_search(parser.parse_trend(trend))
            )
        )
    print(create_message(parser.parse_trend(trend), url))
