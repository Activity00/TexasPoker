# coding: utf-8

"""
@author: 武明辉 
@time: 2018/1/8 19:28
"""
from game.chesscard import Deck


class GameState:
    def __init__(self):
        self.state = 'init'
        self.deck = Deck()

    def start(self):
        self.state = 'preflop'
        self.deal()

    def deal(self):
        pass