# coding: utf-8

"""
@author: 武明辉 
@time: 2018/4/26 15:30
"""
from hashlib import md5

from texas import settings


def get_account_sign(account, ip):
    return md5((account + ip + settings.ACCOUNT_PRI_KEY).encode()).hexdigest()

if __name__ == '__main__':
    pass
