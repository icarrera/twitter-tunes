# -*- coding:utf-8 -*-
try:
    import unittest.mock
except:
    import mock

import pytest
# create_autospec
from ..scripts.twitter_api import call_twitter_api, extract_twitter_trends

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


def test_twitter_okay():
    pass


# def test_final_output():
#     assert len(call_twitter_api()) == len(FINAL_OUTPUT)

# may remove this test when implementing mock
def test_return_type():
    """Test if returned trend list from Twitter API is a list of strings."""
    for trend in call_twitter_api():
        assert isinstance(trend, str)


def test_extract_trends():
    """Test ability to extract only trend names from Twitter API response."""
    assert extract_twitter_trends(RESP_DATA) == FINAL_OUTPUT
