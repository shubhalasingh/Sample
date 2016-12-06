from tornado import gen, web, options
from tornado.httpclient import AsyncHTTPClient, HTTPClient, HTTPRequest, HTTPError
import datetime
import time
import json
import urllib

class DTjsondecoder(json.JSONEncoder):

    """
    This functions encodes objects and return json
    """
    def default(self, obj):
        if isinstance(obj,datetime.datetime):
            return obj.isoformat()
        elif isinstance(obj, datetime.time):
            return str(obj)
        else:
            return json.JSONEncoder.default(self, obj)

class BaseHandler(web.RequestHandler):
    context = {}
    def initialize(self):
        """
            Prepare function. 
            Initialises variables.
            param: cache_dict -> sets the reference cache dict
        """
        self.http_client = AsyncHTTPClient()

    

    @gen.coroutine
    def _get(self, url, response=False , fail_silently=True, **kwargs):
        """
            Fires HTTP query and fetches .
            params:
                url: URL  to hit
                response: response  = True, would return the response object
                            False would return raw response body
                fail_silently: True, would silently log the error
                                False: TBD => raise 

                **kwargs : HTTP kwargs needed fot the hit.
            raises: 
                Response -> a way to return with yield.
            prints: url and time taken for the hit
                  error
        """
        toRespond = response
        
        #start time
        t1 = time.time()
        # print kwargs.get('headers')
        print url
        print '******************************   '
        try:
            response = yield gen.Task(self.http_client.fetch, url,  **kwargs)
            print "****"
            print response
        
        except HTTPError, e:
            #log error
            self.api_error(e, url)
            if toRespond:
                raise HTTPError(e)
                return
            body = {}
        else:   
            #end time
            t2 = time.time()

            #print the url in a different color. Every block should be in diff color.
            # print only in DEBUG mode
            # if var.DEBUG:
            #     color = self.bcolors[
            #     'OKBLUE'] if self.block % 2 == 1 else self.bcolors['HEADER']
            #     print '%s %s %s-------> %ss' % (
            #         color, url.encode('utf-8'), self.bcolors['ENDC'], (t2 - t1))

            # if response.code / 100 != 2:
            #     # print error no matter what the env is.
            #     print '%s error %s in api -- %s %s' % (
            #         self.bcolors['FAIL'], response.code, url.encode('utf-8'),
            #         self.bcolors['ENDC'])
            #     if toRespond:
            #         raise gen.Return(response)
            #     else:
            #         raise gen.Return({})

            if toRespond:
                raise gen.Return(response)
            body = json.loads(response.body)
            # self.write(body)
            # xbody = body['data']['impressions']
            # for d in xbody:
            #     self.write()
        raise gen.Return(body)

    def _post(self, url, body, headers):
        """
            POST method. 
            params:
                url :- url to hit
                data: - postData
        """

        self.Print(url)
        return self.http_client.fetch(
            url,
            method='POST',
            body=body,
            headers=headers
        )


    def _put(self, url, body,headers):
        """
            PUT method. 
            params:
                url :- url to hit
                data: - postData
        """
        self.Print(url)
        #body = urllib.urlencode(body)
        return self.http_client.fetch(
            url,
            method='PUT',
            body=body,
            headers=headers
        )    
