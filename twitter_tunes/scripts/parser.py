import re

def parse_trend(trend):
    """Return a youtube search query based off a twitter trend."""
    trend_re = re.compile(trend)
    return trend_re.sub('#', '')
