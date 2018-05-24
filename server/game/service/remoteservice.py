# coding: utf-8

"""
@author: 武明辉 
@time: 2018/4/26 16:05
"""
import json
from scat import ScatObject
from scat.service import RemoteService


@RemoteService('hall')
def create_room(*args, **kwargs):
    room_mgr = ScatObject.web_root.room_mgr
    room_id = room_mgr.create_room(*args, **kwargs)
    result = {'room_id': room_id}
    return json.dumps(result)


@RemoteService('hall')
def enter_room(room_id, *args, **kwargs):
    room_mgr = ScatObject.web_root.room_mgr
    room_id = room_mgr.enter_room(room_id, *args, **kwargs)
    result = {'room_id': room_id}
    return json.dumps(result)
