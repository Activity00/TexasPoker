# coding: utf-8

"""
@author: 武明辉 
@time: 2018/4/26 14:46
"""
import tornado.web


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

if __name__ == '__main__':
    pass
