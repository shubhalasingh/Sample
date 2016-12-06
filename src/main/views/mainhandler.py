from tornado import gen
import tornado.web
from ..helpers import BaseHandler,DTjsondecoder
import json

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")


class hit_api(BaseHandler):
    """
        endpoint: '/api/v1/hit/'
        req params: url
        resp params: success, status, summary
    """
    @gen.coroutine
    def get(self,flag=0):
        try:
            resp_dict = {"success": True, "data": [], "summary": "hit url"}
            # url = self.get_argument("url")
            url = "http://maps.googleapis.com/maps/api/directions/json?origin=Chicago,IL&destination=Los+Angeles,CA&waypoints=Joplin,MO%7COklahoma+City,OK&sensor=false"
            print "url*************", url 
            response = yield self._get(url)
            a = response
            print a
            # http = tornado.httpclient.AsyncHTTPClient()
            # response = yield http.fetch(url)
            # print response
            print "response######", type(a)
            # resp_dict["data"] = response.body
        except Exception as e:
            print "got exception", str(e)
            resp_dict["success"] = False
            resp_dict["summary"] = str(e)
        finally:
            self.content_type = "application/json"
            self.write(json.dumps(resp_dict, cls=DTjsondecoder))
