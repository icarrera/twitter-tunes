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


def test_generate_youtube_link():
    from youtube_api import generate_youtube_link
    parsed_list = ['dJ8VjyPw0qY',
                   '6ar-7XfCUMo',
                   'jun4rWJ_L6I',
                   'boGvieq9_HI',
                   'E-1jee2laSM',
                   'cVi25pSRAkc',
                   'y2ak_oBeC-I']
    url = generate_youtube_link(parsed_list)
    assert url == 'https://www.youtube.com/watch?v=dJ8VjyPw0qY'
