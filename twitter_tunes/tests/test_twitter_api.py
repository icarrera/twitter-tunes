
# try:
#     import unittest.mock
# except:
#     import mock

import pytest
# create_autospec
from ..scripts.twitter_api import call_twitter_api

FINAL_OUTPUT = ['trend1', 'trend2', 'trend3', 'trend4', 'trend5', 'trend6',
                'trend7', 'trend8', 'trend9', 'trend10'
                ]



def test_twitter_okay():
    pass


# def test_final_output():
#     assert len(call_twitter_api()) == len(FINAL_OUTPUT)

def test_return_type():
    assert isinstance(FINAL_OUTPUT[0], str)
