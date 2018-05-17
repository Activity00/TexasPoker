# coding: utf-8

"""
@author: 武明辉 
@time: 2018/4/27 20:31
"""
from another.game.room import Room


class RoomManager:
    def __init__(self, global_mgr):
        self.global_mgr = global_mgr
        self.room_mapping = {}  # { 房间id: 房间对象 }

    def add_player_to_room(self, player, room):
        if room.id not in self.room_mapping:
            return False
        room.players.append(player)
        return True

    def create_room(self):
        room_id = max(self.room_mapping.keys()) + 1 if self.room_mapping else 0
        room = Room(room_id)
        self.room_mapping[room_id] = room
        return room

    def broadcast(self, room):
        for player in room.players:
            pass


if __name__ == '__main__':
    pass
