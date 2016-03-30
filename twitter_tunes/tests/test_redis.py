# coding=utf-8
import pytest
from twitter_tunes.scripts import redis
from mock import patch


REDIS_PARSE = [
    (b"{'trend3': 'url3', 'trend2': 'url2', 'trend1': 'url1'}",
        {'trend1': 'url1', 'trend2': 'url2', 'trend3': 'url3'}),
    (b"{}", {}),
    (b"{'hello':'its me'}", {'hello': 'its me'}),
]


GOOD_REDIS_RETURN = b"{'trend3': 'url3', 'trend2': 'url2', 'trend1': 'url1'}"
# BAD_REDIS_RETURN = b"hello"


@pytest.mark.parametrize('data, parsed', REDIS_PARSE)
def test_parse_redis_data(data, parsed):
    """Test to see if data dict in bytes is parsed."""
    assert redis.parse_redis_data(data) == parsed


def test_parse_redis_data_error():
    """Test to see if parse redis raises value error if bad input."""
    with pytest.raises(ValueError):
        redis.parse_redis_data(b"this is some data")


@patch('redis.from_url')
def test_get_redis_data_good_redis_key(from_url):
    """Test to see if get redis data returns data dictionary."""
    mock_method = from_url().get
    mock_method.return_value = GOOD_REDIS_RETURN
    assert redis.get_redis_data('trends') == {'trend1': 'url1',
                                              'trend2': 'url2',
                                              'trend3': 'url3'}


@patch('redis.from_url')
def test_get_redis_data_bad_redis_key(from_url):
    """Test to see if get redis data returns data dictionary."""
    mock_method = from_url().get
    mock_method.return_value = None
    assert redis.get_redis_data('bad') == {}
