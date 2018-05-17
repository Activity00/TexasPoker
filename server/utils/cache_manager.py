# coding: utf-8

"""
@author: 武明辉 
@time: 2018/5/7 20:20
"""
from scat.db.cacheclient import CacheUtil


PLAYER_INFO = 'player_info_{}'
LOGIN_PLAYERS = 'login_players'


class CacheManager:
    @staticmethod
    def get_or_set_login_player(_id):
        player_id = CacheUtil.get_client().hget(LOGIN_PLAYERS, _id)
        if not player_id:
            CacheUtil.get_client().hset(LOGIN_PLAYERS, _id)
        return player_id


if __name__ == '__main__':
    pass
