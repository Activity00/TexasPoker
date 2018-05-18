# coding: utf-8

"""
@author: 武明辉 
@time: 2018/2/10 19:37
"""
import json

import tornado.web

from scat import ScatObject
from scat.service import web_service
from utils.common import get_account_sign
from utils.handler import BaseHandler as Handler
from utils.response import APIResponseSuccess, APIResponseError

URL_MAPPINGS = {
    'Login': r'/login/',
    'CreateRoom': r'/create-room/',
    'EnterRoom': r'/enter-room/'

}


class BaseHandler(Handler):
    def prepare(self):
        account = self.get_argument('account')
        sign = self.get_argument('sign')
        if sign != get_account_sign(account, self.request.remote_ip):
            self.write(APIResponseError(status=1000, message='sign 校验失败'))
            self.finish()
            return


@web_service
class Login(BaseHandler):
    URL = URL_MAPPINGS.get('Login')

    def get(self):
        # 获取用户信息
        result = {
            'account': 'xxx',
            'coin': 1000,
        }
        self.write(APIResponseSuccess(result=result))


@web_service
class CreateRoom(BaseHandler):
    URL = URL_MAPPINGS.get('CreateRoom')

    @tornado.web.asynchronous
    def get(self):
        # 返回 game ip port
        df = ScatObject.root.call_child_by_name('game', 'create_room')
        df.addCallback(self.on_response)
        df.addErrback(self.on_error)

    def on_response(self, response):
        result = json.loads(response)
        self.write(APIResponseSuccess(result))
        self.finish()

    def on_error(self, response):
        print(response)
        self.write(APIResponseError(500, message='创建错误', errors=str(response)))
        self.finish()


@web_service
class EnterRoom(BaseHandler):
    URL = URL_MAPPINGS.get('EnterRoom')

    @tornado.web.asynchronous
    def get(self):
       pass