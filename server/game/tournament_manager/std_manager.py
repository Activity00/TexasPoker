# coding: utf-8

"""
@author: 武明辉 
@time: 2018/5/7 16:14
"""


class STDManager:
    def __init__(self, global_mgr):
        self.global_mgr = global_mgr
        self.rooms = {}  # room_id: Room

    def enter_std(self, player_id, data):
        player = self.global_mgr.get_player_from_id(player_id)
        if self.rooms:
            room = self.rooms[0]
        else:
            room = self.global_mgr.create_room()
            self.rooms[room.id] = room

        self.global_mgr.add_player_to_room(player, room)

if __name__ == '__main__':
    pass
