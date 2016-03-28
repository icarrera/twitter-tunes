# coding=utf-8
import pytest


def test_youtube_search():
    from youtube_api import youtube_search
    keyword = 'test search'
    result = youtube_search(keyword)
    assert len(result) > 0


def test_youtube_parse():
    from youtube_api import youtube_parse
    with pytest.raises(AttributeError):
        return youtube_parse([])
