# coding: utf-8

"""
@author: 武明辉 
@time: 2017/12/31 17:36
"""
import tornado.web
from game_server.urls import urls
from game_server.ws_handers import GameHandler

from texas import settings

COOKIE_SECRET = settings.COOKIE_SECRET
DEBUG = settings.DEBUG
config = settings.GAME_SERVER


class HTTPApplication(tornado.web.Application):
    def __init__(self):
        settings = dict({
            'debug': DEBUG,
            'cookie_secret': COOKIE_SECRET
        })
        super(HTTPApplication, self).__init__(handlers=urls, settings=settings)


class WSApplication(tornado.web.Application):
    def __init__(self):
        settings = dict({
            'debug': DEBUG,
            'cookie_secret': COOKIE_SECRET
        })
        super(WSApplication, self).__init__(handlers=[(r'^/game/$', GameHandler)], settings=settings)


if __name__ == '__main__':
    import tornado.ioloop
    http_app = HTTPApplication()
    http_app.listen(config.get('HTTP_PORT'))

    ws_app = WSApplication()
    ws_app.listen(config.get('SOCKET_PORT'))

    tornado.ioloop.IOLoop.current().start()

