import random as r
import helpers as h
import TexasPlayer as pl
from tkinter import PhotoImage

class Texas:
    def __init__(self):
        self.players = []
        for i in range(0, 2):
            self.players.append(pl.TexasPlayer())
        self.pot = 0
        self.table = [None] * 5

    def getChips(self, playerNo):
        return players[playerNo - 1].chips

    def getCards(self, playerNo):
        return players[playerNo - 1].cards

    def bet(self, amount):
        self.pot += amount
        return pot

    def endHand(self, winner):
        self.shuffle()
        players[winner - 1].chips += self.pot
        self.pot = 0

    def shuffle(self):
        cards = h.shuffleDeck()
        players[0].cards = [cards[0], cards[2]]
        players[1].cards = [cards[1], cards[3]]
        self.table = [cards[4], cards[5], cards[6], cards[8], cards[10]]