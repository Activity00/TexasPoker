# coding: utf-8

"""
@author: 武明辉 
@time: 2018/4/25 10:49
"""
from account.model import User, DBSession
from scat.service import web_service
from texas import settings
from utils.common import get_account_sign
from utils.handler import BaseHandler
from utils.response import APIResponseSuccess, APIResponseError

URL_MAPPINGS = {
    'GetServerInfo': r'/get_server_info/',
    'Guest': r'/guest/',

    'Login': r'/login/',
    'Regist': r'/regist/'
}


@web_service
class GetServerInfo(BaseHandler):
    URL = URL_MAPPINGS.get('GetServerInfo')

    def get(self):
        result = {
            'version': settings.VERSION,
            'download_url': settings.DOWNLOAD_URL,
            'hall_addr': settings.HALL_ATTR
        }
        self.write(APIResponseSuccess(result))


@web_service
class Guest(BaseHandler):
    URL = URL_MAPPINGS.get('Guest')

    def get(self, *args, **kwargs):
        account = self.get_argument('account')
        if not account:
            self.write(APIResponseError(status=1000, message='account is None'))
            return

        account = 'guest_' + str(account)
        result = {
            'account': account,
            'sign': get_account_sign(account, self.request.remote_ip)
        }
        self.write(APIResponseSuccess(result))


@web_service
class Regist:
    URL = URL_MAPPINGS.get('Regist')

    def prepare(self):
        self.session = DBSession()

    def get(self):
        user = User(username='xx', password='xx')
        self.session.add(user)
        self.session.commit()

    def post(self):
        params = self.get_body_argument()
        print(params)
        user = User(username='xx', password='xx')
        self.session.add(user)
        self.session.commit()
        self.write({'OK'})

