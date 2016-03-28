import pytest


@pytest.fixture()
def app():
    from twitter_tunes import main
    from webtest import TestApp
    app = main({})
    return TestApp(app)
