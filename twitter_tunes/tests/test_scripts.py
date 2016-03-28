import pytest

TEST_TRENDS = [
    ('#EasterEggRoll', 'EasterEggRoll'),
    ('#ArianaGrade', 'ArianaGrade'),
    ('#mondaymotivation', 'mondaymotivation'),
]


@pytest.mark.parametrize('trend, query', TEST_TRENDS)
def test_parse_trend(trend, query):
    from scripts.parser import parse_trend
    assert parse_trend(trend) == query
