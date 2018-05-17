# coding: utf-8

"""
@author: 武明辉 
@time: 2017/12/26 18:52
"""
from core.response import ResponseSuccess
from status_msg import get_message


def api_login_required(func):
    def wrapper(handler, *args, **kwargs):
        if handler.get_secure_cookie("user"):
            func(handler, *args, **kwargs)
        else:
            return ResponseSuccess(*get_message(1000), errors='请先登陆')
    return wrapper









