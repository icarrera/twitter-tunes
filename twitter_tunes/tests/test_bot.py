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

'''
@mock.patch('twitter_tunes.scripts.twitter_api')
@mock.patch('twitter_tunes.scripts.youtube_api')
@mock.patch('tweepy.API')
def test_make_tweet_main_good(api, twitter_api, youtube_api):
    """Test if bot makes tweet with api data.

    This is what the main function would do.
    """
    from twitter_tunes.scripts import parser, youtube_api, twitter_api
    from twitter_tunes.tests import test_twitter_api

    mock_update_status = api().update_status
    mock_trends = twitter_api()
    mock_yt_search = youtube_api()
    mock_trends.call_twitter_api.return_value = test_twitter_api.FINAL_OUTPUT
    mock_yt_search.get_link.return_value = u"https://www.youtube.com/watch?v=oyEuk8j8imI"

    trends = mock_trends.call_twitter_api()
    top_trend = twitter_bot.choose_trend(trends)
    parse_trend = parser.parse_trend(top_trend)
    # Results that would come from searching this trend.
    # Saved locally to prevent api calls each test.
    url = mock_yt_search.get_link(parse_trend)
    message = twitter_bot.create_message(parse_trend, url)
    twitter_bot.make_tweet(message)
    mock_update_status.assert_called_with(message)
'''

def test_bot_create_message_known_params():
    """Test to see bot can return a message.

    Should contain the trend name and a youtube url.
    """
    url = u'https://www.youtube.com/watch?v=rTfa-9aCTYg'
    message = twitter_bot.create_message(u'A Trend', url)
    assert u'A Trend' in message and url in message

'''
def test_bot_message_function_params():
    """Test to see bot can return a message.

    Message should be based on the returns of other functions.
    """
    from twitter_tunes.scripts import parser, youtube_api
    import twitter_tunes.tests.bot_test_vars as bot_test_vars
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
'''

@mock.patch('twitter_tunes.scripts.twitter_bot.youtube_api.get_link')
def test_bot_choose_trend(get_link):
    """Test choose trend function.

    Should return the 'best' trend from the trends searched by twitter_api.
    Best trend should be the first music related trend it can find.
    """
    from twitter_tunes.tests import bot_test_vars
    from twitter_tunes.scripts import parser

    def yt_side_effect(arg):
        if arg == parser.parse_trend(bot_test_vars.TRENDS[1]):
            return (good_url, True)
        else:
            return (bad_url, False)

    get_link.side_effect = yt_side_effect
    trends = bot_test_vars.TRENDS
    good_url = u'https://www.youtube.com/watch?v=ms2klX-puUU'
    bad_url = u'https://www.youtube.com/watch?v=cU8HrO7XuiE'
    assert twitter_bot.choose_trend(trends)[0] == bot_test_vars.TRENDS[1]
