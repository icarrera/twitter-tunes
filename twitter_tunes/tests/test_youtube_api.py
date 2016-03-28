# coding=utf-8
import pytest


def test_youtube_search():
    from youtube_api import youtube_search
    keyword = 'test search'
    result = youtube_search
    assert 'videoId' in result
