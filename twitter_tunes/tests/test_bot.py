# -*- coding: utf-8 -*-
import pytest
from twitter_tunes.scripts import twitter_bot


def test_bot_create_message_known_params():
    """Test to see bot can return a message.

    Should contain the trend name and a youtube url.
    """
    url = u'https://www.youtube.com/watch?v=rTfa-9aCTYg'
    message = twitter_bot.create_message(u'A Trend', url)
    assert u'A Trend' in message and url in message
