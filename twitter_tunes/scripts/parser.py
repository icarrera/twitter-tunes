import re


def parse_trend(trend):
    """Return a youtube search query based off a twitter trend."""
    trend_no_tag = trend.strip('#')
    spaced_words = trend_no_tag.split(' ')
    final_words = []
    for word in spaced_words:
        final_words.append(parse_camel_trend(word))
    return u' '.join(final_words)


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
        [A-Z]+[a-z]*)  # 1+ uppercase followed by any number of lowercases
        ''', re.VERBOSE)
    words = re.findall(camel_re, trend)
    # Combine the words into a single string seperated by spaces.
    return u' '.join(words)
