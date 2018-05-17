from account_server.hanlders import *

urls = [
    (r'^/guest/$', GuestHandler),
    (r'^/get_server_info/$', GetServerInfoHandler),
]
