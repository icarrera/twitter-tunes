# coding=utf-8
import os
import redis
import json


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


def redis_parse_twitter_trends(trend_list):
    """Parse a list of twitter trends for redis set."""
    clean_trends = []
    for trend in trend_list:
        clean = trend.replace("'", " ")
        clean_trends.append(clean)
    return clean_trends


def set_redis_trend_list(trend_list):
    """Pull trends and set them."""
    clean_trends = redis_parse_twitter_trends(trend_list)
    trend_dict = {'trends': clean_trends}
    set_redis_data('trends', trend_dict)
