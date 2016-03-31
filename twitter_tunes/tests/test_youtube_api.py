# coding=utf-8
from mock import patch
from twitter_tunes.tests import mock_youtube_api_response as API_DATA
from apiclient.errors import HttpError
from httplib2 import ServerNotFoundError
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

VERIFIED = [
    ([('Cdr8_IQqT-E', 'Warner Bros. TV', 'dummy title'),
      ('LDtAIOgBljE', 'Warner Bros. TV', 'dummy title music')], True),
    ([('ObBVYoJY-dA', 'DC Entertainment', 'dummy title'),
      ('8PrDxP5eybo', 'televisionpromosdb', 'dummy title')], False),
    ([('hIyWCxTxPHU', 'televisionpromosdb', 'dummy title'),
      ('_FVwpigX_18', 'Warner Bros. TV', 'dummy title')], False),
    ([('mnC0g9KaPpU', 'The Flash Brasil', 'dummy title'),
      ('_FVwpigX_18', 'Warner Bros. VEVO', 'dummy title')], True),
    ([('qovt8bD1-mw', 'The TSG WB Nexus', 'Obama Song'),
      ('WV5sOc0Gj0w', 'Clevver News', 'dummy dance')], True),
    ([('qovt8bD1-mw', 'The TSG WB Nexus', 'Dummy Title'),
      ('WV5sOc0Gj0w', 'Clevver News', 'other title')], False)
]


@patch('twitter_tunes.scripts.youtube_api.build')
def test_youtube_search_get_data(yt_search):
    """Test to see if we are getting result from search."""
    mock_method = yt_search().search().list().execute
    mock_method.return_value = API_DATA.GOOD_YOUTUBE_RESPONSE
    keyword = 'test search'
    result = youtube_api.youtube_search(keyword)
    assert 'items' in result


@patch('twitter_tunes.scripts.youtube_api.build')
def test_youtube_search_bad_token(yt_search):
    """Test that we get an HttpError is raised with bad youtube search."""
    mock_method = yt_search().search().list().execute
    mock_method.side_effect = HttpError(API_DATA.HTTPERROR_RESP,
                                        API_DATA.HTTPERROR_CONT)
    keyword = 'test search'
    err = youtube_api.youtube_search(keyword)
    assert err.resp == API_DATA.HTTPERROR_RESP
    assert err.content == API_DATA.HTTPERROR_CONT


@patch('twitter_tunes.scripts.youtube_api.build')
def test_youtube_search_no_internet_connection(yt_search):
    """Test if server not found error raised if not connected to internet."""
    mock_method = yt_search().search().list().execute
    mock_method.side_effect = ServerNotFoundError
    keyword = 'test search'
    with pytest.raises(ServerNotFoundError):
        youtube_api.youtube_search(keyword)


def test_youtube_parse_no_data():
    """Test that youtube search parser returns empty list w/ no data input."""
    parsed = youtube_api.youtube_parse([])
    assert parsed == []


def test_youtube_parse_no_search_result():
    """Test that youtube search parser returns empty list w/ no data input."""
    parsed = youtube_api.youtube_parse(API_DATA.BAD_YOUTUBE_RESPONSE)
    assert parsed == []


def test_youtube_parse_good_result():
    """Test that search parser returns list of touples with good api search."""
    parsed = youtube_api.youtube_parse(API_DATA.GOOD_YOUTUBE_RESPONSE)
    assert parsed == [('oyEuk8j8imI', 'JustinBieberVEVO', 'dummy title')]


def test_generate_youtube_link_VEVO_priority():
    """Test link generator prioritizes VEVO links."""
    parsed_list = [(u'kTHNpusq654', u'CapitolMusic', 'dummy title'),
                   (u'tWbLkXhGEmo', u'CapitolMusic', 'dummy title'),
                   (u'wdGZBRAwW74', u'CapitolMusic', 'dummy title'),
                   (u'1-pUaogoX5o', u'emimusic', 'dummy title'),
                   (u'47dtFZ8CFo8', u'CapitalCitiesVEVO', 'dummy title'),
                   (u'xopC0UndnYY', u'Vape Capitol', 'dummy title'),
                   (u'JqNGGsYoXt0', u'West Virginia Public Broadcasting',
                   'dummy title')]
    url = youtube_api.generate_youtube_link(parsed_list)
    assert url[0] == 'https://www.youtube.com/watch?v=47dtFZ8CFo8'


def test_generate_youtube_link_VEVO_good_input():
    """Test URL generator prioritizes first returned link."""
    parsed_list = [(u'oyEuk8j8imI', u'JustinBieberVEVO', 'dummy title'),
                   (u'fRh_vgS2dFE', u'JustinBieberVEVO', 'dummy title'),
                   (u'DK_0jXPuIr0', u'JustinBieberVEVO', 'dummy title'),
                   (u'PfGaX8G0f2E', u'JustinBieberVEVO', 'dummy title'),
                   (u'ztWFp63QPj4', u'The Late Late Show with James Corden',
                   'dummy title'),
                   (u'djzDWMy1z7k', u'JustinBieberVEVO', 'dummy title'),
                   (u'2pvGCUoGXSc', u'Clevver News', 'dummy title'),
                   (u'Kn0YDZ3wifU', u'The Late Late Show with James Corden',
                   'dummy title'),
                   (u'Ca1i6DZC3iY', u'JustinBieberVEVO', 'dummy title')]
    url = youtube_api.generate_youtube_link(parsed_list)
    assert url[0] == 'https://www.youtube.com/watch?v=oyEuk8j8imI'


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
    assert url[0] == 'https://www.youtube.com/watch?v=Cdr8_IQqT-E'


def test_generate_youtube_link_empty_list():
    """Test Lionel Richie returned if no results from search."""
    url = youtube_api.generate_youtube_link([])
    assert url[0] == 'https://www.youtube.com/watch?v=b_ILDFp5DGA'


@patch('twitter_tunes.scripts.youtube_api.build')
def test_get_link_good_data(yt_search):
    mock_method = yt_search().search().list().execute
    mock_method.return_value = API_DATA.GOOD_YOUTUBE_RESPONSE
    keyword = 'Justin Bieber'
    url = youtube_api.get_link(keyword)
    assert url[0] == 'https://www.youtube.com/watch?v=oyEuk8j8imI'


@patch('twitter_tunes.scripts.youtube_api.build')
def test_get_link_bad_data(yt_search):
    mock_method = yt_search().search().list().execute
    mock_method.return_value = API_DATA.BAD_YOUTUBE_RESPONSE
    keyword = 'asdf lawe;lfj'
    url = youtube_api.get_link(keyword)
    assert url[0] == 'https://www.youtube.com/watch?v=b_ILDFp5DGA'


@pytest.mark.parametrize('title, result', TITLES_TERM)
def test_term_checker_0(title, result):
    assert youtube_api.term_checker(title) == result


def test_url_gen():
    assert youtube_api.url_gen(
        '12345') == 'https://www.youtube.com/watch?v=12345'


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
    assert url == ('https://www.youtube.com/watch?v=LDtAIOgBljE', True)


@pytest.mark.parametrize('parsed_list, result', VERIFIED)
def test_get_link_verified(parsed_list, result):
    """Test wether a link is proven to be verified."""
    assert youtube_api.generate_youtube_link(parsed_list)[1] == result
