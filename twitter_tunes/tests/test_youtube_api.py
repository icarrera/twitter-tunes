# coding=utf-8
from mock import patch
from apiclient.errors import HttpError
from twitter_tunes.scripts import youtube_api
import pytest

TITLES_TERM = [
    ('Donald Trump Remix', True),
    ('Donald Trump', False),
    ('300lb Obama', False),
    ('300lb Obama Song', True),
    ('500lb Obama parody', True),
    ('195 fresh piggies', False),
    ('Meow Mix Jam', True),
    ('Meow Mix Dance', True),
    ('Meow Mix Feast', False),
    ('Fresh Piggies Music', True),
    ('', False)
]
BAD_YOUTUBE_RESPONSE = {
    'etag': '"T50iqLU0cleWH2-8bQxaAS2DFh8/ZBV2w65lgyrdAoPQHuFS1_5SrKo"',
    'items': [],
    'kind': 'youtube#searchListResponse',
    'pageInfo': {'resultsPerPage': 10, 'totalResults': 0},
    'regionCode': 'US'}


GOOD_YOUTUBE_RESPONSE = {
    'etag': '"T50iqLU0cleWH2-8bQxaAS2DFh8/rMPhXgkWK6D1tkOLoK27as-vPT0"',
    'items': [{
        'etag': '"T50iqLU0cleWH2-8bQxaAS2DFh8/t65EExZHRMS3i9EoE2pFIrSUw7M"',
        'id': {'kind': 'youtube#video', 'videoId': 'oyEuk8j8imI'},
        'kind': 'youtube#searchResult',
        'snippet': {'channelId': 'UCHkj014U2CQ2Nv0UZeYpE_A',
                    'channelTitle': 'JustinBieberVEVO',
                    'description': "'Purpose' Available Everywhere Now!",
                    'liveBroadcastContent': 'none',
                    'publishedAt': '2015-11-14T15:00:01.000Z',
                    'thumbnails': {
                        'default': {
                            'height': 90,
                            'url': 'https://i.ytimg.com/vi/'
                                   'oyEuk8j8imI/default.jpg',
                            'width': 120},
                        'high': {
                            'height': 360,
                            'url': 'https://i.ytimg.com/vi/'
                                   'oyEuk8j8imI/hqdefault.jpg',
                            'width': 480},
                        'medium': {
                            'height': 180,
                            'url': 'https://i.ytimg.com/vi/'
                                   'oyEuk8j8imI/mqdefault.jpg',
                            'width': 320}},
                    'title': 'dummy title'}}],
    'kind': 'youtube#searchListResponse',
    'nextPageToken': 'CAoQAA',
    'pageInfo': {
        'resultsPerPage': 10, 'totalResults': 1000000},
    'regionCode': 'US'}


HTTPERROR_RESP = {
    'content-type': 'application/json; charset=UTF-8',
    'x-frame-options': 'SAMEORIGIN',
    'status': '400',
    'x-xss-protection': '1; mode=block',
    'x-content-type-options': 'nosniff',
    'cache-control': 'private, max-age=0',
    'alt-svc': 'quic=":443"; ma=2592000; v="31,30,29,28,27,26,25"',
    'transfer-encoding': 'chunked',
    'expires': 'Tue, 29 Mar 2016 20:03:06 GMT',
    'server': 'GSE', 'vary': 'Origin, X-Origin',
    '-content-encoding': 'gzip', 'alternate-protocol': '443:quic,p=1',
    'date': 'Tue, 29 Mar 2016 20:03:06 GMT',
    'content-length': '176'}

HTTPERROR_CONT = b'{\n "error": {\n  "errors": [\n   {\n    "domain":'
' "usageLimits",\n    "reason": "keyInvalid",\n    "message": "Bad'
' Request"\n   }\n  ],\n  "code": 400,\n  "message": "Bad Request"\n }\n}\n'


@patch('twitter_tunes.scripts.youtube_api.build')
def test_youtube_search_get_data(yt_search):
    """Test to see if we are getting result from search."""
    mock_method = yt_search().search().list().execute
    mock_method.return_value = GOOD_YOUTUBE_RESPONSE
    keyword = 'test search'
    result = youtube_api.youtube_search(keyword)
    assert 'items' in result


@patch('twitter_tunes.scripts.youtube_api.build')
def test_youtube_search_bad_token(yt_search):
    """Test that we get an HttpError is raised with bad youtube search."""
    mock_method = yt_search().search().list().execute
    mock_method.side_effect = HttpError(HTTPERROR_RESP, HTTPERROR_CONT)
    keyword = 'test search'
    err = youtube_api.youtube_search(keyword)
    assert err.resp == HTTPERROR_RESP
    assert err.content == HTTPERROR_CONT


def test_youtube_parse_no_data():
    """Test that youtube search parser returns empty list w/ no data input."""
    parsed = youtube_api.youtube_parse([])
    assert parsed == []


def test_youtube_parse_no_search_result():
    """Test that youtube search parser returns empty list w/ no data input."""
    parsed = youtube_api.youtube_parse(BAD_YOUTUBE_RESPONSE)
    assert parsed == []


def test_youtube_parse_good_result():
    """Test that search parser returns list of touples with good api search."""
    parsed = youtube_api.youtube_parse(GOOD_YOUTUBE_RESPONSE)
    assert parsed == [('oyEuk8j8imI', 'JustinBieberVEVO', 'dummy title')]


def test_generate_youtube_link_VEVO_priority():
    """Test link generator prioritizes VEVO links."""
    parsed_list = [(u'kTHNpusq654', u'CapitolMusic', 'dummy title'),
                   (u'tWbLkXhGEmo', u'CapitolMusic', 'dummy title'),
                   (u'wdGZBRAwW74', u'CapitolMusic', 'dummy title'),
                   (u'1-pUaogoX5o', u'emimusic', 'dummy title'),
                   (u'47dtFZ8CFo8', u'CapitalCitiesVEVO', 'dummy title'),
                   (u'xopC0UndnYY', u'Vape Capitol', 'dummy title'),
                   (u'JqNGGsYoXt0', u'West Virginia Public Broadcasting', 'dummy title')]
    url = youtube_api.generate_youtube_link(parsed_list)
    assert url == 'https://www.youtube.com/watch?v=47dtFZ8CFo8'


def test_generate_youtube_link_VEVO_good_input():
    """Test URL generator prioritizes first returned link."""
    parsed_list = [(u'oyEuk8j8imI', u'JustinBieberVEVO', 'dummy title'),
                   (u'fRh_vgS2dFE', u'JustinBieberVEVO', 'dummy title'),
                   (u'DK_0jXPuIr0', u'JustinBieberVEVO', 'dummy title'),
                   (u'PfGaX8G0f2E', u'JustinBieberVEVO', 'dummy title'),
                   (u'ztWFp63QPj4', u'The Late Late Show with James Corden', 'dummy title'),
                   (u'djzDWMy1z7k', u'JustinBieberVEVO', 'dummy title'),
                   (u'2pvGCUoGXSc', u'Clevver News', 'dummy title'),
                   (u'Kn0YDZ3wifU', u'The Late Late Show with James Corden', 'dummy title'),
                   (u'Ca1i6DZC3iY', u'JustinBieberVEVO', 'dummy title')]
    url = youtube_api.generate_youtube_link(parsed_list)
    assert url == 'https://www.youtube.com/watch?v=oyEuk8j8imI'


def test_generate_youtube_link_no_VEVO_good_result():
    """Test link generator to return top result as link."""
    parsed_list = [('Cdr8_IQqT-E', 'Warner Bros. TV', 'dummy title'),
                   ('LDtAIOgBljE', 'Warner Bros. TV', 'dummy title'),
                   ('ObBVYoJY-dA', 'DC Entertainment', 'dummy title'),
                   ('8PrDxP5eybo', 'televisionpromosdb', 'dummy title'),
                   ('hIyWCxTxPHU', 'televisionpromosdb', 'dummy title'),
                   ('_FVwpigX_18', 'Warner Bros. TV', 'dummy title'),
                   ('mnC0g9KaPpU', 'The Flash Brasil', 'dummy title'),
                   ('qovt8bD1-mw', 'The TSG WB Nexus', 'dummy title'),
                   ('WV5sOc0Gj0w', 'Clevver News', 'dummy title'),
                   ('iv02UYr3LCY', 'Supergirl', 'dummy title')]
    url = youtube_api.generate_youtube_link(parsed_list)
    assert url == 'https://www.youtube.com/watch?v=Cdr8_IQqT-E'


def test_generate_youtube_link_empty_list():
    """Test Lionel Richie returned if no results from search."""
    url = youtube_api.generate_youtube_link([])
    assert url == 'https://www.youtube.com/watch?v=b_ILDFp5DGA'


@patch('twitter_tunes.scripts.youtube_api.build')
def test_get_link_good_data(yt_search):
    mock_method = yt_search().search().list().execute
    mock_method.return_value = GOOD_YOUTUBE_RESPONSE
    keyword = 'Justin Bieber'
    url = youtube_api.get_link(keyword)
    assert url == 'https://www.youtube.com/watch?v=oyEuk8j8imI'


@patch('twitter_tunes.scripts.youtube_api.build')
def test_get_link_bad_data(yt_search):
    mock_method = yt_search().search().list().execute
    mock_method.return_value = BAD_YOUTUBE_RESPONSE
    keyword = 'asdf lawe;lfj'
    url = youtube_api.get_link(keyword)
    assert url == 'https://www.youtube.com/watch?v=b_ILDFp5DGA'


@pytest.mark.parametrize('title, result', TITLES_TERM)
def test_term_checker_0(title, result):
    assert youtube_api.term_checker(title) == result


def test_url_gen():
    assert youtube_api.url_gen('12345') == 'https://www.youtube.com/watch?v=12345'


def test_generate_youtube_link_keyword():
    """Test link generator to return top result as link."""
    parsed_list = [('Cdr8_IQqT-E', 'Warner Bros. TV', 'dummy title'),
                   ('LDtAIOgBljE', 'Warner Bros. TV', 'dummy title music'),
                   ('ObBVYoJY-dA', 'DC Entertainment', 'dummy title'),
                   ('8PrDxP5eybo', 'televisionpromosdb', 'dummy title'),
                   ('hIyWCxTxPHU', 'televisionpromosdb', 'dummy title'),
                   ('_FVwpigX_18', 'Warner Bros. TV', 'dummy title'),
                   ('mnC0g9KaPpU', 'The Flash Brasil', 'dummy title'),
                   ('qovt8bD1-mw', 'The TSG WB Nexus', 'dummy title'),
                   ('WV5sOc0Gj0w', 'Clevver News', 'dummy title'),
                   ('iv02UYr3LCY', 'Supergirl', 'dummy title')]
    url = youtube_api.generate_youtube_link(parsed_list)
    assert url == 'https://www.youtube.com/watch?v=LDtAIOgBljE'
