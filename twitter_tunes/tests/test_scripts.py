import pytest

TEST_TRENDS = [
    (u'#EasterEggRoll', u'Easter Egg Roll'),
    (u'#ArianaGrade', u'Ariana Grade'),
    (u'#mondaymotivation', u'mondaymotivation'),
    (u'Nick Swisher', u'Nick Swisher'),
    (u'', u''),
    (u'UFC200 Las Vegas', u'UFC 200 Las Vegas'),
    (u'#Obama', u'Obama')
]


@pytest.mark.parametrize('trend, query', TEST_TRENDS)
def test_parse_trend(trend, query):
    from twitter_tunes.scripts import parser
    assert parser.parse_trend(trend) == query


def test_camel_trend():
    """Test Camel Case is correctly split."""
    from twitter_tunes.scripts import parser
    assert parser.parse_camel_trend(u'MyHotTrend') == u'My Hot Trend'


def test_camel_trend_acronym():
    """Test Acronyms are still grouped and split correctly."""
    from twitter_tunes.scripts import parser
    assert parser.parse_camel_trend(u'MTVEMA') == u'MTVEMA'


def test_camel_trend_mixed():
    """Test both acronyms and regular camel case words."""
    from twitter_tunes.scripts import parser
    assert parser.parse_camel_trend(u'NBAFinals') == u'NBA Finals'


def test_camel_trend_middle_acronym():
    """Test proper splitting when acronym is placed in middle of trend."""
    from twitter_tunes.scripts import parser
    assert parser.parse_camel_trend(u'MyMTVMusic') == u'My MTV Music'


def test_camel_trend_acronym_num():
    """Test proper splitting with acronym and number."""
    from twitter_tunes.scripts import parser
    assert parser.parse_camel_trend(u'UFC200') == u'UFC 200'


def test_camel_trend_special_characters():
    """Test proper splitting with special characters and camel case."""
    from twitter_tunes.scripts import parser
    assert parser.parse_camel_trend(u'I>You') == u'I > You'
