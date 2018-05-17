# coding: utf-8

"""
@author: 武明辉 
@time: 2017/12/31 17:34
"""

import tornado.websocket


class GameHandler(tornado.websocket.WebSocketHandler):

    def prepare(self):
        pass
        # if self.request.headers['Content-Type'].startswith('applications/json'):
        #     self.json_args = json.loads(self.request.body)
        # else:
        #     self.json_args = None

    def check_origin(self, origin):
        return True

    def open(self, *args, **kwargs):
        print('ws opened')

    def on_close(self):
        print('ws closed')

    def on_message(self, message):
        # command, status, message = CommandParse.parse(self, message)
        #
        # print(type(message))
        print(message)
        self.write_message('you said:' + message)
