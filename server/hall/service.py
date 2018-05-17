# coding: utf-8

"""
@author: 武明辉 
@time: 2018/4/25 10:49
"""
import json

import tornado.web

from scat import ScatObject
from scat.service import web_service
from utils.common import get_account_sign
from utils.handler import BaseHandler
from utils.response import APIResponseError, APIResponseSuccess

URL_MAPPINGS = {
    'Login': r'/login/'
}


@web_service
class Login(BaseHandler):
    URL = URL_MAPPINGS.get('Login')

    def prepare(self):
        account = self.get_argument('account')
        sign = self.get_argument('sign')
        if not account or not sign:
            self.finish()

        # TODO check
        # if get_account_sign(account, self.request.remote_ip) != sign:
        #     self.write(APIResponseError(status=1000, message='account sign 不匹配'))
        #     self.finish()

    @tornado.web.asynchronous
    def get(self):
        df = ScatObject.root.call_child_by_name('account', 'get_account_info', self.get_argument('account'))
        df.addCallback(self.on_response)

    def on_response(self, response):
        result = json.loads(response)
        self.write(APIResponseSuccess(result))
        self.finish()
