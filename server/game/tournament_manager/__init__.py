# coding: utf-8

"""
@author: 武明辉 
@time: 2018/5/7 16:13
"""
from game.tournament_manager.player_manager import PlayerManager
from game.tournament_manager.room_manager import RoomManager
from game.tournament_manager.std_manager import STDManager


class GlobalManager:
    def __init__(self):
        self.player_room_mapping = {}  # { 用户id: 房间id }
        self._init_manager()

    def get_player_room(self, player_id):
        return self.player_room_mapping.get(player_id)

    def add_player_to_room(self, player, room):
        self.room_mgr.add_player_to_room(player, room)
        self.player_room_mapping[player.id] = room

    def create_room(self):
        return self.room_mgr.create_room()

    def get_player_from_id(self, player_id):
        return self.player_mgr.get_player_from_id(player_id)

    def _init_manager(self):
        self.player_mgr = PlayerManager(self)
        self.room_mgr = RoomManager(self)
        self.std_mgr = STDManager(self)


if __name__ == '__main__':
    pass
