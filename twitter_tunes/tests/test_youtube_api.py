# coding=utf-8
import pytest
import youtube_api


# SOME OF THESE SEARCHES SHOULD BE ADDED TO CONFTEST TO REDUCE API CALLS #


# def test_youtube_search_get_data():
#     """Test to see if we are getting result from search."""
#     keyword = 'test search'
#     result = youtube_search(keyword)
#     assert len(result) > 0
#
#
# def test_youtube_search_no_results():
#     """Test if you get empty item list from search with no results."""
#     keyword = 'asdf safvdafvdsvafs'
#     result = youtube_search(keyword)
#     assert result.get('items') == []


def test_youtube_parse_no_data():
    """Test that youtube search parser returns empty list with no data input"""
    parsed = youtube_api.youtube_parse([])
    assert parsed == []


def test_generate_youtube_link_VEVO_priority():
    """Test link generator prioritizes VEVO links"""
    parsed_list = [('kTHNpusq654', 'CapitolMusic'),
                   ('tWbLkXhGEmo', 'CapitolMusic'),
                   ('wdGZBRAwW74', 'CapitolMusic'),
                   ('1-pUaogoX5o', 'emimusic'),
                   ('47dtFZ8CFo8', 'CapitalCitiesVEVO'),
                   ('xopC0UndnYY', 'Vape Capitol'),
                   ('JqNGGsYoXt0', 'West Virginia Public Broadcasting')]
    url = youtube_api.generate_youtube_link(parsed_list)
    assert url == 'https://www.youtube.com/watch?v=47dtFZ8CFo8'


def test_generate_youtube_link_no_VEVO():
    """Test URL generator prioritizes first returned link"""
    parsed_list = [('oyEuk8j8imI', 'JustinBieberVEVO'),
                   ('fRh_vgS2dFE', 'JustinBieberVEVO'),
                   ('DK_0jXPuIr0', 'JustinBieberVEVO'),
                   ('PfGaX8G0f2E', 'JustinBieberVEVO'),
                   ('ztWFp63QPj4', 'The Late Late Show with James Corden'),
                   ('djzDWMy1z7k', 'JustinBieberVEVO'),
                   ('2pvGCUoGXSc', 'Clevver News'),
                   ('Kn0YDZ3wifU', 'The Late Late Show with James Corden'),
                   ('Ca1i6DZC3iY', 'JustinBieberVEVO')]
    url = youtube_api.generate_youtube_link(parsed_list)
    assert url == 'https://www.youtube.com/watch?v=oyEuk8j8imI'


def test_generate_youtube_link_empty_list():
    """Test Lionel Richie returned if no results from search"""
    url = youtube_api.generate_youtube_link([])
    assert url == 'https://www.youtube.com/watch?v=b_ILDFp5DGA'
