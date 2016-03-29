# -*- coding: utf-8 -*-
try:
    import unittest.mock as mock
except:
    import mock
from twitter_tunes.scripts import twitter_bot


@mock.patch('tweepy.API')
def test_make_tweet_static_message(api):
    """Test if bot makes tweet with a set message."""
    mock_method = api().update_status
    twitter_bot.make_tweet(u"more tests")
    mock_method.assert_called_with(u"more tests")


@mock.patch('tweepy.API')
def test_make_tweet_main(api):
    """Test if bot makes tweet with api data.

    This is what the main function would do.
    """
    from twitter_tunes.scripts import parser, youtube_api
    mock_method = api().update_status
    import bot_test_vars
    top_trend = twitter_bot.choose_trend(bot_test_vars.TRENDS)
    parse_trend = parser.parse_trend(top_trend)
    # Results that would come from searching this trend.
    # Saved locally to prevent api calls each test.
    search_results = bot_test_vars.N_A_SEARCH_RESULTS
    url = youtube_api.generate_youtube_link(
        youtube_api.youtube_parse(
                search_results
            )
        )
    message = twitter_bot.create_message(parse_trend, url)
    twitter_bot.make_tweet(message)
    mock_method.assert_called_with(message)


def test_bot_create_message_known_params():
    """Test to see bot can return a message.

    Should contain the trend name and a youtube url.
    """
    url = u'https://www.youtube.com/watch?v=rTfa-9aCTYg'
    message = twitter_bot.create_message(u'A Trend', url)
    assert u'A Trend' in message and url in message


def test_bot_message_function_params():
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


def test_bot_choose_trend():
    """Test choose trend function.

    Should return the first trend from the trends searched by twitter_api.
    """
    import bot_test_vars
    trends = bot_test_vars.TRENDS
    assert twitter_bot.choose_trend(trends) == trends[0]