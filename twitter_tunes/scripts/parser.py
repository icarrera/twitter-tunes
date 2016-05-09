import re


def parse_trend(trend):
    """Return a youtube search query based off a twitter trend."""
    trend_no_tag = trend.strip('#')
    spaced_words = trend_no_tag.split(' ')
    return u' '.join([parse_camel_trend(x) for x in spaced_words])
    # TODO-STRETCH GOAL: function that parses out a lowercase no spaced trend.


def parse_camel_trend(trend):
    """Return string with spaces based off camelcase/acronyms.

    'MyHotTrend' would return 'My Hot Trend'
    'NBAFinals' would return 'NBA Finals'
    'MTV' would return 'MTV'
    'UFC200 would return UFC 200'
    """
    # Split the trend into words based off regex groups.
    camel_re = re.compile(r'''
        (\W+|  # One or more non-word characters
        \d+|  # One or more digit characters
        # 1+ uppercase followed by 1+ uppercase and 1+ lowercases
        [A-Z]+(?=[A-Z]+[a-z]+)|
        [a-z]+(?=[^a-z])|  # lowercase letters followed by non-lowercase chars
        (?<=[^a-z])[a-z]+|  # lowercase word preceded by non-lowercase chars
        [A-Z]+[a-z]*) # 1+ uppercase followed by any number of lowercases
        ''', re.VERBOSE)
    words = re.findall(camel_re, trend)
    # Combine the words into a single string seperated by spaces.
    if words:
        return u' '.join(words)
    # if it's lowercase no spaced just return it back.
    return trend
