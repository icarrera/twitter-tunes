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


def test_bot_function_params():
    """Test to see bot can return a message.

    Message should be based on the returns of other functions.
    """
    from twitter_tunes.scripts import parser, youtube_api
    import bot_test_vars
    trend = u"#StoryFromNorthAmerica"
    parse_trend = parser.parse_trend(trend)
    # Results that would come from searching this trend.
    # Saved locally to prevent api calls each test.
    search_results = bot_test_vars.N_A_SEARCH_RESULTS
    url = youtube_api.generate_youtube_link(
        youtube_api.youtube_parse(
                search_results
            )
        )
    message = twitter_bot.create_message(parse_trend, url)
    assert (u'Story From North America' in message and
            u'https://www.youtube.com/watch?v=ms2klX-puUU' in message)
