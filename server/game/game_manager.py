# coding: utf-8

"""
@author: 武明辉 
@time: 2018/4/9 13:30
"""
from game.deck import Deck
from game.game_state import InitState


class GameManager:
    def __init__(self):
        self._game_state = InitState(self)
        self._deck = Deck()

    def set_state(self, state):
        self._game_state = state

    def start(self):
        print('start')

    def check(self):
        self._game_state.check()

    def fapai(self):
        self._game_state.fapai()


if __name__ == '__main__':
    game_manager = GameManager()
    game_manager.fapai()
    game_manager.fapai()
