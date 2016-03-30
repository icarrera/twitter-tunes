# coding=utf-8
import os
import redis
import json


def parse_redis_data(data):
    try:
        dat_decoded = data.decode('utf-8')
        json_string = dat_decoded.replace("'", "\"")
        data_dict = json.loads(json_string)
        return data_dict
    except ValueError:
        print('No data to parse.')
        raise ValueError


def get_redis_data(key):
    REDIS_URL = os.environ.get('REDIS_URL')
    redis_conn = redis.from_url(REDIS_URL)
    value = redis_conn.get(key)
    if value is None:
        return {}
    else:
        parsed_redis = parse_redis_data(value)
        return parsed_redis


def set_redis_data(key, val):
    REDIS_URL = os.environ.get('REDIS_URL')
    redis_conn = redis.from_url(REDIS_URL)
    redis_conn.set(key, val)
