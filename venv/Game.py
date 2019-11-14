import random
import Player
import HumanPlayer
import helpers

class Game:
    def __init__(self, playerNo = 1):
        self.player = Player.Player()
        self.player.train(10000)
        self.humanPlayer = HumanPlayer.HumanPlayer()
        self.deal()
        self.player.takeChips(1)
        self.humanPlayer.takeChips(1)
        self.pot = 2

    def bet(self, p = "c"):
        if p == "h":
            self.humanPlayer.takeChips(1)
        self.pot += 1

    def reset(self, type):
        win = ""
        if type == "show":
            if self.humanPlayer.card > self.player.card:
                self.humanPlayer.giveChips(self.pot)
                win="h"
            else:
                self.player.giveChips(self.pot)
                win = "c"
        elif type == "AIfold":
            self.humanPlayer.giveChips(self.pot)
        elif type == "Hfold":
            self.player.giveChips(self.pot)
        self.deal()
        self.player.takeChips(1)
        self.humanPlayer.takeChips(1)
        self.pot = 2
        return win

    def deal(self):
        newCards = helpers.shuffle([1, 2, 3])
        self.humanPlayer.card, self.player.card = newCards[0], newCards[1]
