# -*- coding:utf-8 -*-
try:
    import unittest.mock as mock
except:
    import mock
from six import string_types
import unittest
import pytest
# create_autospec
from ..scripts.twitter_api import call_twitter_api, extract_twitter_trends
from ..scripts.twitter_api import WOEID_US

RESP_DATA = [{'words': 'words_value',
              'trends': [
                         {'name': 'trend1', 'key2': 'value1'},
                         {'name': 'trend2', 'key2': 'value2'},
                         {'name': 'trend3', 'key2': 'value3'},
                         {'name': 'trend4', 'key2': 'value4'},
                         {'name': 'trend5', 'key2': 'value4'},
                         {'name': 'trend6', 'key2': 'value4'},
                         {'name': 'trend7', 'key2': 'value4'},
                         {'name': 'trend8', 'key2': 'value4'},
                         {'name': 'trend9', 'key2': 'value4'},
                         {'name': 'trend10', 'key2': 'value4'},
                        ]
              }]

FINAL_OUTPUT = ['trend1', 'trend2', 'trend3', 'trend4', 'trend5', 'trend6',
                'trend7', 'trend8', 'trend9', 'trend10'
                ]


# @pytest.fixture(scope='function')
# def bad_auth():
#     consumerKey = 'NOPE'
#     consumerSecret = 'NOT'
#     accessToken = 'NEVER'
#     return consumerKey, consumerSecret, accessToken
#
#
# def test_bad_response(bad_auth):
#     assert call_twitter_api() == 'Missing OAuth key or token'


@mock.patch('tweepy.API')
def test_final_output(api):
    """Test if length of our call_twitter_api list is as expected."""
    mocked_method = api().trends_place
    mocked_method.return_value = RESP_DATA
    assert len(call_twitter_api()) == len(FINAL_OUTPUT)


@mock.patch('tweepy.API')
def test_return_type(api):
    """Test if returned trend list from Twitter API is a list of strings."""
    mocked_method = api().trends_place
    mocked_method.return_value = RESP_DATA
    for trends in call_twitter_api():
        mocked_method.assert_called_once_with(WOEID_US)
        for trend in trends:
            assert isinstance(trend, string_types)
        assert isinstance(trend, string_types)


def test_extract_trends():
    """Test ability to extract only trend names from Twitter API response."""
    assert extract_twitter_trends(RESP_DATA) == FINAL_OUTPUT
