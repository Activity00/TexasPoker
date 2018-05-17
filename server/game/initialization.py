# coding: utf-8

"""
@author: 武明辉 
@time: 2018/4/25 10:48
"""
from scat import ScatObject
from scat.utils.token_manager import TokenManager
from texas import settings

ScatObject.web_root.token_mgr = TokenManager(settings.TOKEN_PRI_KEY)

if __name__ == '__main__':
    pass
