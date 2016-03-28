# coding=utf-8
import pytest


def test_youtube_search():
    from youtube_api import youtube_search
    keyword = 'test search'
    result = youtube_search(keyword)
    assert len(result) > 0


def test_youtube_search_no_results():
    from youtube_api import youtube_search
    keyword = 'asdf safvdafvdsvafs'
    result = youtube_search(keyword)
    assert result.get('items') == []


def test_youtube_search():
    from youtube_api import youtube_search



def test_youtube_parse_no_data():
    from youtube_api import youtube_parse
    parsed = youtube_parse([])
    assert parsed == []


def test_generate_youtube_link_VEVO_priority():
    from youtube_api import generate_youtube_link
    parsed_list = [('kTHNpusq654', 'CapitolMusic'),
                   ('tWbLkXhGEmo', 'CapitolMusic'),
                   ('wdGZBRAwW74', 'CapitolMusic'),
                   ('1-pUaogoX5o', 'emimusic'),
                   ('47dtFZ8CFo8', 'CapitalCitiesVEVO'),
                   ('xopC0UndnYY', 'Vape Capitol'),
                   ('JqNGGsYoXt0', 'West Virginia Public Broadcasting')]
    url = generate_youtube_link(parsed_list)
    assert url == 'https://www.youtube.com/watch?v=47dtFZ8CFo8'


def test_generate_youtube_link_no_VEVO():
    from youtube_api import generate_youtube_link
    parsed_list = [('kTHNpusq654', 'CapitolMusic'),
                   ('tWbLkXhGEmo', 'CapitolMusic'),
                   ('wdGZBRAwW74', 'CapitolMusic'),
                   ('1-pUaogoX5o', 'emimusic'),
                   ('xopC0UndnYY', 'Vape Capitol'),
                   ('JqNGGsYoXt0', 'West Virginia Public Broadcasting')]
    url = generate_youtube_link(parsed_list)
    assert url == 'https://www.youtube.com/watch?v=47dtFZ8CFo8'


def test_generate_youtube_link_empty_list():
    from youtube_api import generate_youtube_link
    url = generate_youtube_link([])
    assert url == 'https://www.youtube.com/watch?v=b_ILDFp5DGA'
