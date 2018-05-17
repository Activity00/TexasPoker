import hashlib

import tornado.web
from core.response import ResponseSuccess
from extensions import DB_Session
from models.User import User

from texas import settings

config = settings.ACCOUNT_SERVER


class BaseHandler(tornado.web.RequestHandler):
    def data_received(self, chunk):
        pass

    def set_default_headers(self):
        # 设置允许跨域访问
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "x-requested-with")
        self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')

    def get_current_user(self):
        return self.get_secure_cookie("user")


class DBBaseHandler(BaseHandler):
    def initialize(self):
        self.session = DB_Session()

    def on_finish(self):
        self.session.close()


class GuestHandler(DBBaseHandler):

    def get(self):
        # user = self.current_user
        account = "guest_" + self.get_argument('account')
        sign = hashlib.md5((account + self.request.remote_ip + config['ACCOUNT_PRI_KEY']).encode()).hexdigest()
        data = {
            'account': account,
            'hall_ip': config['HALL_IP'],
            'sign': sign
        }
        user = self.session.query(User).filter(User.nickname == account).first()
        if user:
            print(user)
            data.update({
                'id': user.id,
                'name': user.nickname,
                'coin': user.coin,
                'diamond': user.diamond
            })
            self.write(ResponseSuccess(data))
            return

        user = User(nickname=account, password='123456', coin=1000, diamond=100)
        self.session.add(user)
        self.session.commit()
        data.update({
            'id': user.id,
            'name': user.nickname,
            'coin': user.coin,
            'diamond': user.diamond
        })

        self.set_secure_cookie("user", self.get_argument(user.account))
        self.write(ResponseSuccess(data))


class GetServerInfoHandler(BaseHandler):
    def get(self, *args, **kwargs):
        data = {
            'version': config['VERSION'],
            'hall_ip': config['HALL_IP'],
            'appweb': config['APP_WEB'],
        }
        self.write(ResponseSuccess(data))

