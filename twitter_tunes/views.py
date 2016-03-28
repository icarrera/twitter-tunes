from pyramid.view import view_config
from twitter_tunes.scripts import parser


@view_config(route_name='home', renderer='templates/main_template.jinja2')
def my_view(request):
    return {'query': parser.parse_trend('#TwitterTunesRules')}
