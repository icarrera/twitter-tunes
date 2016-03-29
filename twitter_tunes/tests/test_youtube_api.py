# coding=utf-8
from mock import MagicMock

from twitter_tunes.scripts import youtube_api


BAD_YOUTUBE_RESPONSE = {
    'etag': '"q5k97EMVGxODeKcDgp8gnMu79wM/ZBV2w65lgyrdAoPQHuFS1_5SrKo"',
    'items': [],
    'kind': 'youtube#searchListResponse',
    'pageInfo': {'resultsPerPage': 10, 'totalResults': 0},
    'regionCode': 'US'
    }


GOOD_YOUTUBE_RESPONSE = {
    'etag': '"q5k97EMVGxODeKcDgp8gnMu79wM/CPBLCHO4TGGvyVAPOao1conn7xo"',
    'items': [
        {'etag': '"q5k97EMVGxODeKcDgp8gnMu79wM/t65EExZHRMS3i9EoE2pFIrSUw7M"',
         'id': {'kind': 'youtube#video', 'videoId': 'oyEuk8j8imI'},
         'kind': 'youtube#searchResult',
         'snippet': {'channelId': 'UCHkj014U2CQ2Nv0UZeYpE_A',
                     'channelTitle': 'JustinBieberVEVO',
                     'description': "'Purpose' Available Everywhere Now! iTunes: http://smarturl.it/PurposeDlx?IQid=VEVO1113 Stream & Add To Your Spotify Playlist: http://smarturl.it/sPurpose?",
                     'liveBroadcastContent': 'none',
                     'publishedAt': '2015-11-14T15:00:01.000Z',
                     'thumbnails': {'default': {'height': 90,
                                                'url': 'https://i.ytimg.com/vi/oyEuk8j8imI/default.jpg',
                                                'width': 120},
                                    'high': {'height': 360,
                                             'url': 'https://i.ytimg.com/vi/oyEuk8j8imI/hqdefault.jpg',
                                             'width': 480},
                                    'medium': {'height': 180,
                                               'url': 'https://i.ytimg.com/vi/oyEuk8j8imI/mqdefault.jpg',
                                               'width': 320}},
        'title': 'Justin Bieber - Love Yourself  (PURPOSE : The Movement)'}}],
    'kind': 'youtube#searchListResponse',
    'nextPageToken': 'CAEQAA',
    'pageInfo': {'resultsPerPage': 1, 'totalResults': 1000000},
    'regionCode': 'US'}


# SOME OF THESE SEARCHES SHOULD BE ADDED TO CONFTEST TO REDUCE API CALLS #


youtube_search = MagicMock(name='youtube_search',
                           return_value=GOOD_YOUTUBE_RESPONSE)


def test_youtube_search_get_data():
    """Test to see if we are getting result from search."""
    keyword = 'test search'
    result = youtube_search(keyword)
    assert len(result) > 0


youtube_search = MagicMock(name='youtube_search',
                           return_value=BAD_YOUTUBE_RESPONSE)


def test_youtube_search_no_results():
    """Test if you get empty item list from search with no results."""
    keyword = 'asdf safvdafvdsvafs'
    result = youtube_search(keyword)
    assert result.get('items') == []


def test_youtube_parse_no_data():
    """Test that youtube search parser returns empty list with no data input."""
    parsed = youtube_api.youtube_parse([])
    assert parsed == []


def test_youtube_parse_no_search_result():
    """Test that youtube search parser returns empty list with no data input."""
    parsed = youtube_api.youtube_parse(BAD_YOUTUBE_RESPONSE)
    assert parsed == []


def test_youtube_parse_good_result():
    """Test that search parser returns list of touples with good api search."""
    parsed = youtube_api.youtube_parse(GOOD_YOUTUBE_RESPONSE)
    assert parsed == [('oyEuk8j8imI', 'JustinBieberVEVO')]


def test_generate_youtube_link_VEVO_priority():
    """Test link generator prioritizes VEVO links."""
    parsed_list = [(u'kTHNpusq654', u'CapitolMusic'),
                   (u'tWbLkXhGEmo', u'CapitolMusic'),
                   (u'wdGZBRAwW74', u'CapitolMusic'),
                   (u'1-pUaogoX5o', u'emimusic'),
                   (u'47dtFZ8CFo8', u'CapitalCitiesVEVO'),
                   (u'xopC0UndnYY', u'Vape Capitol'),
                   (u'JqNGGsYoXt0', u'West Virginia Public Broadcasting')]
    url = youtube_api.generate_youtube_link(parsed_list)
    assert url == 'https://www.youtube.com/watch?v=47dtFZ8CFo8'


def test_generate_youtube_link_VEVO_good_input():
    """Test URL generator prioritizes first returned link."""
    parsed_list = [(u'oyEuk8j8imI', u'JustinBieberVEVO'),
                   (u'fRh_vgS2dFE', u'JustinBieberVEVO'),
                   (u'DK_0jXPuIr0', u'JustinBieberVEVO'),
                   (u'PfGaX8G0f2E', u'JustinBieberVEVO'),
                   (u'ztWFp63QPj4', u'The Late Late Show with James Corden'),
                   (u'djzDWMy1z7k', u'JustinBieberVEVO'),
                   (u'2pvGCUoGXSc', u'Clevver News'),
                   (u'Kn0YDZ3wifU', u'The Late Late Show with James Corden'),
                   (u'Ca1i6DZC3iY', u'JustinBieberVEVO')]
    url = youtube_api.generate_youtube_link(parsed_list)
    assert url == 'https://www.youtube.com/watch?v=oyEuk8j8imI'


def test_generate_youtube_link_no_VEVO_good_result():
    """Test link generator to return top result as link."""
    parsed_list = [('Cdr8_IQqT-E', 'Warner Bros. TV'),
                   ('LDtAIOgBljE', 'Warner Bros. TV'),
                   ('ObBVYoJY-dA', 'DC Entertainment'),
                   ('8PrDxP5eybo', 'televisionpromosdb'),
                   ('hIyWCxTxPHU', 'televisionpromosdb'),
                   ('_FVwpigX_18', 'Warner Bros. TV'),
                   ('mnC0g9KaPpU', 'The Flash Brasil'),
                   ('qovt8bD1-mw', 'The TSG WB Nexus'),
                   ('WV5sOc0Gj0w', 'Clevver News'),
                   ('iv02UYr3LCY', 'Supergirl')]
    url = youtube_api.generate_youtube_link(parsed_list)
    assert url == 'https://www.youtube.com/watch?v=Cdr8_IQqT-E'


def test_generate_youtube_link_empty_list():
    """Test Lionel Richie returned if no results from search."""
    url = youtube_api.generate_youtube_link([])
    assert url == 'https://www.youtube.com/watch?v=b_ILDFp5DGA'
