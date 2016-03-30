# coding=utf-8
import os
import redis
import json


def parse_redis_data(data):
    dat_decoded = data.decode('utf-8')
    json_string = dat_decoded.replace("'", "\"")
    data_dict = json.loads(json_string)
    return data_dict


def get_redis_data(key):
    REDIS_URL = os.environ.get('REDIS_URL')
    redis_conn = redis.from_url(REDIS_URL)
    value = redis_conn.get(key)
    parsed_redis = parse_redis_data(value)
    return parsed_redis


def set_redis_data(key, val):
    REDIS_URL = os.environ.get('REDIS_URL')
    redis_conn = redis.from_url(REDIS_URL)
    redis_conn.set(key, val)
