# coding: utf-8

"""
@author: 武明辉 
@time: 2018/2/10 19:38
"""

from scat import ScatObject
from scat.service import root_service


@root_service
def hert_beat(self, server_info):
    """ 接受游戏服务器信息 """
    pass


@root_service
def register_server(server_info):
    """ 接受游戏服务器信息 """
    mapping = ScatObject.web_root.room_server_mapping = {}  # name: {ip, port, load}
    mapping.update(server_info)

