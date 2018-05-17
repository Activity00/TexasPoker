# coding: utf-8

"""
@author: 武明辉 
@time: 2017/12/23 14:36
"""
import tornado.web
from account_server.urls import urls

from texas import settings

COOKIE_SECRET = settings.COOKIE_SECRET
config = settings.ACCOUNT_SERVER


class Application(tornado.web.Application):
    def __init__(self):
        settings = dict({
            'debug': True,
            'cookie_secret': COOKIE_SECRET
        })
        super(Application, self).__init__(handlers=urls, settings=settings)


if __name__ == '__main__':
    import tornado.ioloop
    app = Application()
    app.listen(config.get('CLIENT_PORT'))
    tornado.ioloop.IOLoop.current().start()

