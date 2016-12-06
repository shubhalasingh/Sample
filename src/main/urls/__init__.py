from ..views import *
from tornado.web import url

url_patterns = [
    url(r'/', MainHandler, name='index-page'),
    url(r'/api/v1/hit/', hit_api, name="hit-page"),
]