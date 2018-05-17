# coding: utf-8

"""
@author: 武明辉 
@time: 2018/1/8 16:50
"""
from random import randint


class Card:
    """
        黑桃:spade
        红桃:heart
        方片:diamond
        草花:club
    """
    SUITS = ['S', 'H', 'D', 'C']

    def __init__(self, value, suit):
        self.suit = suit
        self.value = value

    def __str__(self):
        return self.suit + str(self.value)


def create_cards():
    cards = []
    for s in Card.SUITS:
        for v in range(2, 15):
            cards.append(Card(v, s))

    return cards


class Deck:
    CARDS = create_cards()

    def __init__(self, shuffling_algorithm=None):
        self.cards = self.shuffling(shuffling_algorithm)

    def shuffling(self, shufflshuffling_algorithm):
        if shufflshuffling_algorithm:
            if not hasattr(shufflshuffling_algorithm, '__call__'):
                raise ValueError('shufflshuffling_algorithm is not a method')
            self.cards = shufflshuffling_algorithm(self.CARDS.copy())
            if not isinstance(self.cards, list):
                raise ValueError('shufflshuffling_algorithm must return a list instance')
        else:
            return self.fisher_yates_shuffle(self.CARDS.copy())

    @staticmethod
    def fisher_yates_shuffle(cards):
        n = len(cards)
        for i in range(n - 1, 0, -1):
            j = randint(0, i)
            cards[j], cards[i] = cards[i], cards[j]
        return cards

    def take(self, num_of_card, draw_num=0, draw_append=False):
        """
        take cards
        :param num_of_card:
        :param draw_num: drop card
        :param draw_append:  if drop card append the deck ends
        :return: cards list
        """
        for _ in range(draw_num):
            if draw_append:
                self.cards.append(self.cards.pop(0))
            else:
                self.cards.pop(0)

        return [self.cards.pop(0) for _ in range(num_of_card)]


if __name__ == '__main__':
    d = Deck()
    print(d.cards)
    print(d.take(-1))


