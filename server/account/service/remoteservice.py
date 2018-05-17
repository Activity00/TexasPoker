# coding: utf-8

"""
@author: 武明辉 
@time: 2018/4/26 16:05
"""
import json

from account.model import User, DBSession
from scat.service import RemoteService


@RemoteService('hall')
def get_account_info(account):
    if not account:
        return json.dumps({})
    session = DBSession()
    user = session.query(User).filter_by(username=account).first()
    return user.to_json() if user else json.dumps({})
