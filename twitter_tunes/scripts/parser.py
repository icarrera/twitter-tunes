import re


def parse_trend(trend):
    """Return a youtube search query based off a twitter trend."""
    trend_no_tag = trend.strip('#')
    # TODO: new function dealing with camel case
    return trend_no_tag


def parse_camel_trend(trend):
    """Return string with spaces based off camelcase/acronyms.

    'MyHotTrend' would return 'My Hot Trend'
    'NBAFinals' would return 'NBA Finals'
    'MTV' would return 'MTV'
    """
    camel_re = re.compile(r'''
        (\W+|
        \d+|
        [A-Z]+(?=[A-Z]+[a-z]+)|
        [A-Z]+[a-z]*)
        ''', re.VERBOSE)
    words = re.findall(camel_re, trend)
    return u' '.join(words)
