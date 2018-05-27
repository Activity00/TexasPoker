# coding: utf-8

"""
@author: 武明辉 
@time: 2018/5/10 16:07
"""
import json

from scat import ScatObject
from scat.service import master_service


@master_service
def get_token(player_id, life_time):
    token_mgr = ScatObject.web_root.token_mgr
    token = token_mgr.produce_token(player_id, life_time)
    return json.dumps({'token': token})


if __name__ == '__main__':
    pass
