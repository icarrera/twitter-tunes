import re


def parse_trend(trend):
    """Return a youtube search query based off a twitter trend."""
    return trend.strip('#')
