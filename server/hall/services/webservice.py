# coding: utf-8

"""
@author: 武明辉 
@time: 2018/2/10 19:37
"""

from scat.service import web_service
from utils.common import get_account_sign
from utils.handler import BaseHandler as Handler
from utils.response import APIResponseSuccess, APIResponseError

URL_MAPPINGS = {
    'Login': r'/login/',
    'CreateRoom': r'/create-room/',
    'EnterRoom': r'enter-room/'

}


class BaseHandler(Handler):
    def prepare(self):
        account = self.get_argument('account')
        sign = self.get_argument('sign')
        if not account or sign:
            self.write(APIResponseError(status=1000, message='account or sign can not be None'))
            self.finish()
            return

        check = sign == get_account_sign(account, self.request.remote_ip)
        if not check:
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

    def get(self):
        # 返回房间号码
        pass

    def post(self):
        pass


@web_service
class EnterRoom(BaseHandler):
    URL = URL_MAPPINGS.get('EnterRoom')

    def get(self):
        # 返回房间号码
        pass

    def post(self):
        pass


