# coding: utf-8

"""
@author: 武明辉 
@time: 2018/4/25 10:48
"""
from tornado import ioloop

from scat import ScatObject
from scat.utils.token_manager import TokenManager
from texas import settings

ScatObject.web_root.token_mgr = TokenManager(settings.TOKEN_PRI_KEY)


def register_server_info():
    server_info = {'name': 'xxoo'}
    dd = ScatObject.remote['hall'].call_remote("register_server", server_info)


ioloop.PeriodicCallback(register_server_info, 1000 * 10).start()


if __name__ == '__main__':
    pass
