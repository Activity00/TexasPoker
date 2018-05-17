# coding: utf-8

"""
@author: 武明辉 
@time: 2018/4/9 14:04
"""
from game.Player import Player
from game.game_manager import GameManager


class IGameType:
    pass


class FastGame(IGameType):
    def __init__(self, *args, **kwargs):
        self._game_manager = GameManager()
        self.room = None
        self.players = []

    def enter(self, player_id):
        if player_id in self.players:
            print('xxoo')
            return

        player = Player(player_id)
        self.players.append(player)

    def start(self):
        if not self.players:
            return

        self._game_manager.start()

    def check(self):
        self._game_manager.check()

    def chupai(self):
        self._game_manager.fapai()

if __name__ == '__main__':
    pass
