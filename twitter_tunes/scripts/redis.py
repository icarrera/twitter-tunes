# coding=utf-8
import os
import redis
import json
from twitter_tunes.scripts import twitter_api
from twitter_tunes.scripts import youtube_api
from twitter_tunes.scripts import parser


REDIS_URL = os.environ.get('REDIS_URL')


def parse_redis_data(data):
    """Parse redis data into data dictionary."""
    try:
        dat_decoded = data.decode('utf-8')
        json_string = dat_decoded.replace("'", "\"")
        data_dict = json.loads(json_string)
        return data_dict
    except ValueError:
        print('No data to parse.')
        raise ValueError


def get_redis_data(key):
    """Get redis data from Heroku."""
    value = redis.from_url(REDIS_URL).get(key)
    if value is not None:
        parsed_redis = parse_redis_data(value)
        return parsed_redis
    return {}


def set_redis_data(key, val):
    """Set redis data in Heroku."""
    redis_conn = redis.from_url(REDIS_URL)
    redis_conn.set(key, val)


def trend_parse_redis(trend_list):
    """Parse a list of twitter trends for redis set."""
    clean_trends = []
    for trend in trend_list:
        clean = trend.replace("'", " ")
        clean_trends.append(clean)
    return clean_trends


def youtube_links_redis(trend_list):
    """Return youtube link for twitter trend."""
    youtube_list = []
    for trend in trend_list:
        parsed_trend = parser.parse_trend(trend)
        youtube_url = youtube_api.get_link(parsed_trend)
        youtube_list.append(youtube_url)
    return youtube_list


def main():
    """Pull trends and set them."""
    trend_list = twitter_api.call_twitter_api()
    clean_trends = trend_parse_redis(trend_list)
    trend_dict = {'trends': clean_trends}

    yt_links = youtube_links_redis(clean_trends)

    set_redis_data('trends', trend_dict)
