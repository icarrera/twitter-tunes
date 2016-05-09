# -*- coding: utf-8 -*-
try:
    import unittest.mock as mock
except:
    import mock
from twitter_tunes.scripts import twitter_bot
from twitter_tunes.tests import bot_test_vars
import pytest


def redis_side_effect(arg):
        if arg == u'trends':
            return bot_test_vars.REDIS_TRENDS
        elif arg == u'last_tweets':
            return bot_test_vars.REDIS_LAST_POSTS[:]


@mock.patch('tweepy.API')
def test_make_tweet_static_message(api):
    """Test if bot makes tweet with a set message."""
    mock_method = api().update_status
    twitter_bot.make_tweet(u"more tests")
    mock_method.assert_called_with(u"more tests")


@mock.patch('twitter_tunes.scripts.twitter_bot.redis_data.set_redis_data')
@mock.patch('twitter_tunes.scripts.twitter_bot.redis_data.get_redis_data')
@mock.patch('twitter_tunes.scripts.twitter_bot.youtube_api.get_link')
@mock.patch('twitter_tunes.scripts.twitter_api')
@mock.patch('tweepy.API')
def test_main_good(api, twitter_api, get_link, get_redis_data,
                   set_redis_data):
    """Test if bot makes tweet with api data.

    This is what the main function would do.
    """
    from twitter_tunes.tests import test_twitter_api
    test_url = u"https://www.youtube.com/watch?v=oyEuk8j8imI"
    mock_update_status = api().update_status
    mock_trends = twitter_api()
    mock_trends.call_twitter_api.return_value = test_twitter_api.FINAL_OUTPUT
    get_link.return_value = (test_url, True)
    get_redis_data.side_effect = redis_side_effect

    redis_trends = get_redis_data(u'trends')
    trends = redis_trends[u'trends']
    da_trend, url = twitter_bot.choose_trend(trends)
    message = twitter_bot.create_message(da_trend, url)
    twitter_bot.make_tweet(message)
    mock_update_status.assert_called_with(message)


@mock.patch('twitter_tunes.scripts.twitter_bot.redis_data.set_redis_data')
@mock.patch('twitter_tunes.scripts.twitter_bot.redis_data.get_redis_data')
@mock.patch('twitter_tunes.scripts.twitter_bot.twitter_api.call_twitter_api')
@mock.patch('twitter_tunes.scripts.twitter_bot.youtube_api.get_link')
@mock.patch('tweepy.API')
def test_main_bad_twitter(api, youtube_api, call_twitter_api, get_redis_data,
                          set_redis_data):
    """Test if main does stuff if twitter goes horribly wrong.

    Make sure it can keep going."""
    get_redis_data.return_value = {}
    youtube_api.return_value = (u'url', True)
    call_twitter_api.side_effect = ValueError('Missing OAuth key or token.')
    assert twitter_bot.main() == u'Something went horribly wrong.'


@mock.patch('twitter_tunes.scripts.twitter_bot.redis_data.set_redis_data')
@mock.patch('twitter_tunes.scripts.twitter_bot.redis_data.get_redis_data')
@mock.patch('twitter_tunes.scripts.twitter_api')
@mock.patch('twitter_tunes.scripts.twitter_bot.youtube_api.get_link')
@mock.patch('twitter_tunes.scripts.twitter_bot.tweepy.API.update_status')
def test_main_bad_update(update_status, youtube_api, twitter_api,
                         get_redis_data, set_redis_data):
    """Test if main does stuff if tweepy goes horribly wrong.

    Make sure it can keep going."""
    from tweepy import TweepError
    get_redis_data.side_effect = redis_side_effect
    youtube_api.return_value = (u'url', True)
    update_status.side_effect = TweepError("Couldn't Post")
    assert twitter_bot.main() == u'Something went horribly wrong.'


@mock.patch('twitter_tunes.scripts.twitter_bot.redis_data.set_redis_data')
@mock.patch('twitter_tunes.scripts.twitter_bot.redis_data.get_redis_data')
@mock.patch('twitter_tunes.scripts.twitter_api')
@mock.patch('twitter_tunes.scripts.youtube_api')
@mock.patch('twitter_tunes.scripts.twitter_bot.tweepy.API.trends_place')
def test_main_bad_get_trends(trends_place, yt, tw, get, set):
    """Test if main does stuff if tweepy goes horribly wrong.

    Make sure it can keep going."""
    from tweepy import RateLimitError
    get.return_value = {}
    trends_place.side_effect = RateLimitError("Slow Down!")
    assert twitter_bot.main() == u'Something went horribly wrong.'


@mock.patch('twitter_tunes.scripts.twitter_bot.redis_data.set_redis_data')
@mock.patch('twitter_tunes.scripts.twitter_bot.redis_data.get_redis_data')
@mock.patch('twitter_tunes.scripts.twitter_api')
@mock.patch('tweepy.API')
@mock.patch('twitter_tunes.scripts.twitter_bot.youtube_api.youtube_search')
def test_main_bad_youtube(youtube_search, tweepy, ta, get, set):
    """Test if main does stuff if twitter goes horribly wrong.

    Make sure it can keep going."""
    get.side_effect = redis_side_effect
    from apiclient.errors import HttpError
    youtube_search.side_effect = HttpError('Uhh', b'youtube broke.')
    assert twitter_bot.main() == u'Something went horribly wrong.'


@mock.patch('twitter_tunes.scripts.twitter_bot.redis_data.get_redis_data')
def test_main_bad_redis(get_redis_data):
    """Test if main does stuff if redis goes horribly wrong."""
    from requests.exceptions import ConnectionError
    get_redis_data.side_effect = ConnectionError
    assert twitter_bot.main() == u'Something went horribly wrong.'


def test_bot_create_message_known_params():
    """Test to see bot can return a message.

    Should contain the trend name and a youtube url.
    """
    url = u'https://www.youtube.com/watch?v=rTfa-9aCTYg'
    message = twitter_bot.create_message(u'A Trend', url)
    assert u'A Trend' in message and url in message


@mock.patch('twitter_tunes.scripts.youtube_api.get_link')
def test_bot_message_function_params(get_link):
    """Test to see bot can return a message.

    Message should be based on the returns of other functions.
    """
    from twitter_tunes.scripts import parser
    trend = u"#StoryFromNorthAmerica"
    parse_trend = parser.parse_trend(trend)
    # Results that would come from searching this trend.
    # Saved locally to prevent api calls each test.
    get_link.return_value = (u'https://www.youtube.com/watch?v=ms2klX-puUU',
                             True)
    url = get_link(parse_trend)
    message = twitter_bot.create_message(trend, url[0])
    assert (u'#StoryFromNorthAmerica' in message and
            u'https://www.youtube.com/watch?v=ms2klX-puUU' in message)


@mock.patch('twitter_tunes.scripts.twitter_bot.redis_data.set_redis_data')
@mock.patch('twitter_tunes.scripts.twitter_bot.redis_data.get_redis_data')
@mock.patch('twitter_tunes.scripts.twitter_bot.youtube_api.get_link')
def test_bot_choose_trend(get_link, get_redis_data, set_redis_data):
    """Test choose trend function.

    Should return the 'best' trend from the trends searched by twitter_api.
    Best trend should be the first music related trend it can find.
    """
    from twitter_tunes.scripts import parser

    def yt_side_effect(arg):
        if arg == parser.parse_trend(bot_test_vars.TRENDS[1]):
            return (good_url, True)
        elif arg == parser.parse_trend(bot_test_vars.TRENDS[2]):
            return (good_url, True)
        else:
            return (bad_url, False)

    get_link.side_effect = yt_side_effect
    get_redis_data.side_effect = redis_side_effect
    redis_trends = get_redis_data(u'trends')
    trends = redis_trends[u'trends']
    good_url = u'https://www.youtube.com/watch?v=ms2klX-puUU'
    bad_url = u'https://www.youtube.com/watch?v=cU8HrO7XuiE'
    assert twitter_bot.choose_trend(trends)[0] == bot_test_vars.TRENDS[2]  # trend you expect.


@mock.patch('twitter_tunes.scripts.twitter_bot.redis_data.set_redis_data')
@mock.patch('twitter_tunes.scripts.twitter_bot.redis_data.get_redis_data')
@mock.patch('twitter_tunes.scripts.twitter_bot.youtube_api.get_link')
def test_bot_choose_trend_bad_redis(get_link, get_redis_data, set_redis_data):
    """test if the choosing trend handles a bad redis call."""
    get_link.return_value = (u'url', True)

    def redis_side_effect_bad(arg):
        if arg == u'trends':
            return bot_test_vars.REDIS_TRENDS
        elif arg == u'last_tweets':
            return {}

    get_redis_data.side_effect = redis_side_effect_bad
    redis_trends = get_redis_data(u'trends')
    trends = redis_trends[u'trends']
    assert twitter_bot.choose_trend(trends)[0] == bot_test_vars.TRENDS[0]


@mock.patch('twitter_tunes.scripts.twitter_bot.redis_data.set_redis_data')
@mock.patch('twitter_tunes.scripts.twitter_bot.redis_data.get_redis_data')
@mock.patch('twitter_tunes.scripts.twitter_bot.youtube_api.get_link')
def test_bot_choose_trend_trend_long(get_link, get_redis_data, set_redis_data):
    """test if the choosing trend handles a long last_tweets"""
    get_link.return_value = (u'url', True)

    def redis_side_effect_bad(arg):
        if arg == u'trends':
            return bot_test_vars.REDIS_TRENDS
        elif arg == u'last_tweets':
            return [u'trend', u'trend', u'trend', u'trend', u'trend']

    get_redis_data.side_effect = redis_side_effect_bad
    redis_trends = get_redis_data(u'trends')
    trends = redis_trends[u'trends']
    assert twitter_bot.choose_trend(trends)[0] == bot_test_vars.TRENDS[0]


@mock.patch('twitter_tunes.scripts.twitter_bot.tweepy.API.update_status')
def test_make_tweet_bad(update_status):
    """Test if make_tweet breaks."""
    import twitter_tunes.scripts.twitter_bot as bot
    old_key = bot.consumerKey
    bot.consumerKey = None
    with pytest.raises(ValueError):
        twitter_bot.make_tweet('Please dont post')
    bot.consumerKey = old_key
