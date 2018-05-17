# coding: utf-8

"""
@author: 武明辉 
@time: 2018/4/27 17:13
"""
from collections import Iterable

from utils.response import CommandResponseSuccess


class Player:
    def __init__(self, _id):
        self.id = _id
        self.stacks = 1000

    @property
    def coin(self):
        pass

    @property
    def stacks(self):
        pass


class PlayerManager:
    def __init__(self, global_mgr):
        self.global_mrg = global_mgr
        self.players = {}  # player_id : Player
        self.online_player_num = 0

    def login_player(self, player_id, socket):
        print('xxx')
        if player_id not in self.players:
            player = Player(player_id)
            player.socket = socket
            self.players[player_id] = player
            self.online_player_num += 1
        self.notify(player_id, CommandResponseSuccess('login_result'))

    def exit_player(self, socket):
        self.players.pop(socket.player_id, None)
        socket.player_id = None
        self.online_player_num -= 1

    def get_player_from_id(self, player_id):
        return self.players.get(player_id)

    def notify(self, player_info, response):
        if not isinstance(player_info, Iterable):
            player_info = tuple(player_info)
        for info in player_info:
            _id = player_info
            if isinstance(_id, Player):
                _id = info.id
            player = self.get_player_from_id(int(_id))
            if player and player.socoet and player.socket.ws_connection:
                player.socket.write_message(response)




def broadcast(players, message):
    receivers = []
    protocol_ids = []
    for player in players:
        if player.protocol.connected:
            receivers.append(player.player_id)
            protocol_ids.append(player.protocol.protocol_id)

    data = {'receivers': receivers, 'protocol_ids': protocol_ids, 'line': str(message)}
    conn = get_redis_connection('redis')
    conn.rpush('player_message_queue', json.dumps(data))


def notify(player, message):
    if player.protocol.connected:
        data = {'receivers': [player.player_id], 'protocol_ids': [player.protocol.protocol_id], 'line': str(message)}
        conn = get_redis_connection('redis')
        conn.rpush('player_message_queue', json.dumps(data))
