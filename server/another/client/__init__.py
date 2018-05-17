from tornado.httpserver import HTTPServer
from tornado.web import Application
import tornado.websocket


class MyHandler(tornado.web.RequestHandler):

    def set_default_headers(self):
        # 设置允许跨域访问
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header('Access-Control-Allow-Credentials', "True")
        self.set_header("Access-Control-Allow-Headers", "Origin, X-Requested-With, Content-Type, Accept")
        self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')

        print('烦烦烦')
        # return True

    def get(self):
        self.set_status(200)
        print('xxoo')
        self.write('hello')


class OtherHandler(tornado.websocket.WebSocketHandler):
    def get(self, *args, **kwargs):
        print('xxxxxxx')

    def check_origin(self, origin):
        return True

    def open(self, *args, **kwargs):
        print('open')

    def on_message(self, message):
        print('message')

    def finish(self, chunk=None):
        print('finish')


if __name__ == '__main__':
    import tornado.ioloop
    app = Application(handlers=[(r'/socket.io/', MyHandler), (r'/', OtherHandler)])
    server = HTTPServer(app)
    server.listen(10001)
    tornado.ioloop.IOLoop.current().start()
