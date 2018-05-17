# coding: utf-8

"""
@author: 武明辉 
@time: 2018/4/9 13:44
"""


class IGameState:
    def __init__(self, game_manager):
        self._game_manager = game_manager

    def check(self):
        raise NotImplementedError

    def fapai(self):
        raise NotImplementedError


class InitState(IGameState):
    def fapai(self):
        print('init fapai')
        self._game_manager.set_state(PreFlopState(self._game_manager))

    def check(self):
        print('init check')


class PreFlopState(IGameState):
    def fapai(self):
        print('pre papai')

    def check(self):
        pass


class FlopState(IGameState):
    def fapai(self):
        pass

    def check(self):
        pass


class TurnState(IGameState):
    def fapai(self):
        pass

    def check(self):
        pass


class RiverState(IGameState):
    def fapai(self):
        pass

    def check(self):
        pass


if __name__ == '__main__':
    pass
