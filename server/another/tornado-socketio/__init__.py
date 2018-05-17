# coding: utf-8

"""
@author: 武明辉 
@time: 2018/1/13 10:42
"""
import tornado.websocket
import tornado.web
from tornado.log import gen_log
from tornado.web import Application


class Firsthandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.write('000')
        print('xxxx')


class SocketIOHandler(tornado.websocket.WebSocketHandler):

    def __init__(self, application, request, **kwargs):
        super(SocketIOHandler, self).__init__(application, request, **kwargs)

        # self.request.headers['Upgrade'] = 'websocket'
        # self.request.headers['Connection'] = self.request.headers.get('Connection') + ',upgrade'
        #
        # self.request.headers['Sec-Websocket-Key'] = 'x'
        # self.request.headers['Sec-Websocket-Version'] = 'x'
        # self.request.headers["Sec-WebSocket-Version"] = '13'

    @tornado.web.asynchronous
    def get(self, *args, **kwargs):
        print(self.request.headers)
        self.open_args = args
        self.open_kwargs = kwargs

        # Upgrade header should be present and should be equal to WebSocket
        if self.request.headers.get("Upgrade", "").lower() != 'websocket':
            self.set_status(400)
            log_msg = "Can \"Upgrade\" only to \"WebSocket\"."
            self.finish(log_msg)
            gen_log.debug(log_msg)
            return

        # Connection header should be upgrade.
        # Some proxy servers/load balancers
        # might mess with it.
        headers = self.request.headers
        connection = map(lambda s: s.strip().lower(),
                         headers.get("Connection", "").split(","))
        if 'upgrade' not in connection:
            self.set_status(400)
            log_msg = "\"Connection\" must be \"Upgrade\"."
            self.finish(log_msg)
            gen_log.debug(log_msg)
            return

        # Handle WebSocket Origin naming convention differences
        # The difference between version 8 and 13 is that in 8 the
        # client sends a "Sec-Websocket-Origin" header and in 13 it's
        # simply "Origin".
        if "Origin" in self.request.headers:
            origin = self.request.headers.get("Origin")
        else:
            origin = self.request.headers.get("Sec-Websocket-Origin", None)

        # If there was an origin header, check to make sure it matches
        # according to check_origin. When the origin is None, we assume it
        # did not come from a browser and that it can be passed on.
        if origin is not None and not self.check_origin(origin):
            self.set_status(403)
            log_msg = "Cross origin websockets not allowed"
            self.finish(log_msg)
            gen_log.debug(log_msg)
            return

        self.ws_connection = self.get_websocket_protocol()
        if self.ws_connection:
            self.ws_connection.accept_connection()
        else:
            self.set_status(426, "Upgrade Required")
            self.set_header("Sec-WebSocket-Version", "7, 8, 13")
            self.finish()

    def prepare(self):
        pass

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
        print('xxxxx', message)
        # self.write_message('you said:' + message)

    def on(self):
        raise NotImplementedError


if __name__ == '__main__':
    import tornado.ioloop
    app = Application(handlers=[('/socket.io/', Firsthandler), ('/', SocketIOHandler)], debug=True)
    app.listen(10001)

    tornado.ioloop.IOLoop.current().start()