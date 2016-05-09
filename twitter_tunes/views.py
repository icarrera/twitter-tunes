from pyramid.view import view_config
from twitter_tunes.scripts import parser, youtube_api
from twitter_tunes.scripts.redis_data import get_redis_data


@view_config(route_name='home', renderer='templates/index.jinja2')
def home(request):
    return get_redis_data('trends')


@view_config(route_name='video', renderer='json')
def get_youtube_url(request):
    """Return YT url of a specific trend."""
    trend = request.matchdict['trend']
    search_term = parser.parse_trend(trend)
    url, validated = youtube_api.get_link(search_term)
    url = url.replace('watch?v=', 'embed/')
    return {'url': url, 'validated': str(validated).lower()}
