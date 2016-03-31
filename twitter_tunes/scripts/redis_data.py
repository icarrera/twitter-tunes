# coding=utf-8
import os
import redis
import json


REDIS_URL = os.environ.get('REDIS_URL')


def parse_redis_data(data):
    """Parse redis data into data dictionary."""
    try:
        dat_decoded = data.decode('utf-8')
        json_string = dat_decoded.replace("u\"", "\"")
        data_list = json.loads(json_string)
        return data_list
    except ValueError:
        print('No data to parse.')
        raise ValueError


def get_redis_data(key):
    """Get redis data from Heroku."""
    value = redis.from_url(REDIS_URL).get(key)
    if value is not None:
        parsed_redis = parse_redis_data(value)
        return parsed_redis
    return []


def set_redis_data(key, val):
    """Set redis data in Heroku."""
    redis_conn = redis.from_url(REDIS_URL)
    redis_conn.set(key, json.dumps(val))
