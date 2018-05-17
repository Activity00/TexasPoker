# coding: utf-8

"""
@author: 武明辉 
@time: 2018/1/8 18:53
"""
import random

from another.game.mgr.game_mgr import GameMgr


class Room:
    def __init__(self, size=9):
        # self.id = id
        # self.create_time = time.time()
        # self.conf = conf
        self.size = size
        self.seat_range_set = {i for i in range(self.size)}
        self.seats = {}  # int(0~8): Player
        self.players = []
        self.game_mgr = GameMgr()

    def seat_player(self, player, position=None):
        if 0 >= position < self.size:
            return False

        position = random.choice(list(self.seat_range_set - set(self.seats.keys())))
        self.seats[position] = player
        return position
