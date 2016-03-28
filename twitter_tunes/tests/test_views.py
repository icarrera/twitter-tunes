import pytest


def test_view_html(app):
    """Test if main view returns html."""
    response = app.get('/')
    assert response.html
