import pytest


def test_view_html(app):
    """Test if main view returns html."""
    response = app.get('/')
    assert response.html


def test_view_unit_trends():
    """Unit test ensuring list of trends is returned."""
    from twitter_tunes.views import home
    response = home('my_request')
    assert isinstance(response['trends'], list)
