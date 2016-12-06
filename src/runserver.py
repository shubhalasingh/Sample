import tornado.ioloop
import tornado.web
import tornado.httpserver
from main.urls import url_patterns
from main.settings import temp_settings as st, options


class Sample(tornado.web.Application):
    def __init__(self):
        # print urls.url_patterns
        tornado.web.Application.__init__(self, url_patterns, **st)  
   

if __name__ == "__main__":
    app = Sample()
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.bind(options.port)
    print 'running on port %s' % options.port
    print 'running on debug %s' % options.debug

    if st["debug"]:
        http_server.start()
    else:
        http_server.start(0)
    gl = tornado.ioloop.IOLoop.instance()
    gl.start()