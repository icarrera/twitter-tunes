from pyramid.testing import DummyRequest
from mock import patch
from twitter_tunes.tests import mock_youtube_api_response as API_DATA


def test_view_html(app):
    """Test if main view returns html."""
    response = app.get('/')
    assert response.html


def test_view_unit_trends():
    """Unit test ensuring list of trends is returned."""
    from twitter_tunes.views import home
    response = home('my_request')
    assert isinstance(response['trends'], list)


@patch('twitter_tunes.scripts.youtube_api.build')
def test_view_get_youtube_url_unit(yt_search):
    """Test correct information is returned upon an ajax request."""
    from twitter_tunes.views import get_youtube_url
    mock_method = yt_search().search().list().execute
    mock_method.return_value = API_DATA.GOOD_YOUTUBE_RESPONSE
    req = DummyRequest()
    req.matchdict = {'trend': 'anything'}
    response = get_youtube_url(req)
    assert response == {'url': 'https://www.youtube.com/embed/oyEuk8j8imI',
                        'validated': 'true'}
