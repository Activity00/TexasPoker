# coding: utf-8

"""
@author: 武明辉 
@time: 2017/12/27 10:44
"""
CODE_MSG = {
    '1000': '授权失败'
}


def get_message(status):
    return status, CODE_MSG.get(status, '')
