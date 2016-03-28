import pytest

TEST_TRENDS = [
    ('#EasterEggRoll', 'EasterEggRoll'),
    ('#ArianaGrade', 'ArianaGrade'),
    ('#mondaymotivation', 'mondaymotivation'),
]


@pytest.mark.parametrize('trend, query', TEST_TRENDS)
def test_parse_trend(trend, query):
    from twitter_tunes.scripts import parser
    assert parser.parse_trend(trend) == query
