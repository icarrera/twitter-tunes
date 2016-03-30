# coding=utf-8
import pytest
from twitter_tunes.scripts import redis


REDIS_PARSE = [
    (b"{'trend3': 'url3', 'trend2': 'url2', 'trend1': 'url1'}",
        {'trend1': 'url1', 'trend2': 'url2', 'trend3': 'url3'}),
    (b"{}", {}),
    (b"{'hello':'its me'}", {'hello': 'its me'}),
]


@pytest.mark.parametrize('data, parsed', REDIS_PARSE)
def test_parse_redis_data(data, parsed):
    assert redis.parse_redis_data(data) == parsed


def test_parse_redis_data_error():
    with pytest.raises(ValueError):
        redis.parse_redis_data(b"this is some data")
