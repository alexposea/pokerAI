import helpers

class HumanPlayer:
    def __init__(self, name = "Player", chips = 10):
        self.name = name
        self.chips = chips
        self.card = 0

    def getChips(self):
        return self.chips

    def takeChips(self, amount = 1):
        if self.chips >= amount:
            self.chips -= amount
            return self.chips
        return -1

    def giveChips(self, amount):
        self.chips += amount
        return self.chips