import re


def parse_trend(trend):
    """Return a youtube search query based off a twitter trend."""
    trend_no_tag = trend.strip('#')
    # TODO: new function dealing with camel case
    return trend_no_tag


def parse_camel_trend(trend):
    """Return string with spaces based off camelcase.

    'MyHotTrend' would return 'My Hot Trend'
    """
    camel_re = re.compile(r'(?=[A-Z][^A-Z])')
    words = camel_re.split(trend)
    import pdb; pdb.set_trace()
    return u' '.join(words) 
