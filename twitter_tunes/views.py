from pyramid.view import view_config
from twitter_tunes.scripts import parser, youtube_api


@view_config(route_name='home', renderer='templates/index.jinja2')
def home(request):
    # trends = twitter_api.call_twitter_api()
    trends = ['one two step', '#two', 'kyrie', '#DogsInTheRoom', 'Patty Duke',
              '#Trends', '#TwitterTunes', '#Hashtag', '#Lunch Time', '#TGIF']
    return {'trends': trends}


def get_topics(request):
    """return dict of twitter trends."""
    # Make API request to twitter for top trends.
    # return that.
    pass


@view_config(route_name='video', renderer='json')
def get_youtube_url(request):
    """Return YT url of a specific trend."""
    trend = request.matchdict['trend']
    search_term = parser.parse_trend(trend)
    url = youtube_api.get_link(search_term)[0]
    print(url)
    url = url.replace('watch?v=', 'embed/')
    print(url)
    return {'url': url}
