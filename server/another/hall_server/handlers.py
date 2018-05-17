# coding: utf-8

"""
@author: 武明辉 
@time: 2017/12/26 18:27
"""
import tornado.web
import tornado.httpclient
import tornado.escape

from core.auth import api_login_required
from extensions import DB_Session


class BaseHandler(tornado.web.RequestHandler):
    def data_received(self, chunk):
        pass

    def set_default_headers(self):
        # 设置允许跨域访问
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "x-requested-with")
        self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')

    def get_current_user(self):
        pass


class DBBaseHandler(BaseHandler):
    def initialize(self):
        self.session = DB_Session()

    def on_finish(self):
        self.session.close()


class CreateTournamentHandler(BaseHandler):
    @api_login_required
    @tornado.web.asynchronous
    def get(self):
        http = tornado.httpclient.AsyncHTTPClient()
        http.fetch("http://friendfeed-api.com/v2/feed/bret",
                   callback=self.on_response)

    def on_response(self, response):
        if response.error: raise tornado.web.HTTPError(500)
        json = tornado.escape.json_decode(response.body)
        self.write(json)
        self.finish()

    @tornado.gen.coroutine
    def get(self):
        http = tornado.httpclient.AsyncHTTPClient()
        response = yield http.fetch("http://friendfeed-api.com/v2/feed/bret")
        json = tornado.escape.json_decode(response.body)
        self.write("Fetched " + str(len(json["entries"])) + " entries "
                                                            "from the FriendFeed API")

    def on_connection_close(self):
        pass

