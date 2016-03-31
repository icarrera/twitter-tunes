# -*- coding:utf-8 -*-
try:
    import unittest.mock as mock
except:
    import mock
from six import string_types
import pytest
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


FINAL_OUTPUT = [u'trend1', u'trend2', u'trend3', u'trend4', u'trend5', u'trend6',
                u'trend7', u'trend8', u'trend9', u'trend10'
                ]

BAD_WOEID = [None, 1111111111111111111111111111111, 0, 12345678, 'blahblah']


@pytest.mark.parametrize("bad_woeid", BAD_WOEID)
def test_invalid_woeid(bad_woeid):
    """Raise TweepError if Twitter location ID is invalid."""
    import twitter_tunes.scripts.twitter_api as tapi
    from tweepy import TweepError
    old_WOEID = tapi.WOEID_US
    tapi.WOEID_US = bad_woeid
    with pytest.raises(TweepError):
        call_twitter_api()
    tapi.WOEID_US = old_WOEID


def test_missing_key():
    """Raise ValueError if any keys or tokens are missing."""
    import twitter_tunes.scripts.twitter_api as tapi
    old_key = tapi.consumerKey
    tapi.consumerKey = None
    with pytest.raises(ValueError):
        call_twitter_api()
    tapi.consumerKey = old_key


def test_no_response(mocker):
    """Raise TweepError if Twitter is down."""
    from tweepy import TweepError
    mocked_api = mocker.patch('tweepy.API')
    mocked_method = mocked_api().trends_place
    mocked_method.side_effect = TweepError("Failed to send request: %s' % e")
    with pytest.raises(TweepError):
        call_twitter_api()


def test_final_output(mocker):
    """Test if length of our call_twitter_api list is as expected."""
    mocked_api = mocker.patch('tweepy.API')
    mocked_method = mocked_api().trends_place
    mocked_method.return_value = RESP_DATA
    assert len(call_twitter_api()) == len(FINAL_OUTPUT)


def test_return_type(mocker):
    """Test if returned trend list from Twitter API is a list of strings."""
    mocked_api = mocker.patch('tweepy.API')
    mocked_method = mocked_api().trends_place
    mocked_method.return_value = RESP_DATA
    for trends in call_twitter_api():
        mocked_method.assert_called_once_with(WOEID_US)
        for trend in trends:
            assert isinstance(trend, string_types)
        assert isinstance(trend, string_types)


def test_extract_trends(mocker):
    """Test ability to extract only trend names from Twitter API response."""
    mocked_api = mocker.patch('tweepy.API')
    mocked_method = mocked_api().trends_place
    mocked_method.return_value = RESP_DATA
    assert extract_twitter_trends(RESP_DATA) == FINAL_OUTPUT
