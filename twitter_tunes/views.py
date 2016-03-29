from pyramid.view import view_config
from twitter_tunes.scripts import parser


@view_config(route_name='home', renderer='templates/main_template.jinja2')
def my_view(request):
    return {}


def get_topics(request):
    """return dict of twitter trends."""
    # Make API request to twitter for top trends.
    # return that.
    pass


def get_youtube_url(request):
    """Return YT url of a specific trend."""
    # Get trend out of ajax.
    # parse the trend.
    # get youtube url from the query.
    # return that.
    pass
