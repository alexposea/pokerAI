import helpers
import random
import Action
import Node

class Player():
    def __init__(self, name = "CPU", chips = 10):
        self.name = name
        self.chips = chips
        self.nodeMap = {}
        self.card = 0

    def nextAction(self, history):
        infoSet = str(self.card) + history
        avgStrat = self.nodeMap[infoSet].getAverageStrategy()
        opt = ["pass", "bet"]
        c = random.choices(population = opt, weights = avgStrat, k = 1)
        if c == "pass" or self.chips == 0:
            return "pass"
        self.chips -= 1
        return "bet"

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

    def train(self, iteration):
        cards = [1, 2, 3]
        util = 0.0
        for i in range(0, iteration):
            cards = helpers.shuffle(cards)
            util += self.cfr(cards, "", 1.0, 1.0)
        print("Average game value: " + str(util / iteration))
        for key in self.nodeMap:
            print(self.nodeMap[key])

    def cfr(self, cards, history, p0, p1):
        plays = len(history)
        player = plays % 2
        opponent = 1 - player

        if plays > 1:
            if history[-2:] == "pp":
                if cards[player] > cards[opponent]:
                    return 1.0
                return -1.0
            elif history[-2:] == "bb":
                if cards[player] > cards[opponent]:
                    return 2.0
                return -2.0
            elif history[-2:] == "bp":
                return 1.0

        infoSet = str(cards[player]) + history

        if infoSet in self.nodeMap:
            node = self.nodeMap[infoSet]
        else:
            node = Node.Node(infoSet)
            self.nodeMap[infoSet] = node

        strategy = node.getStrategy(p0 if player == 0 else p1)
        util = [0.0] * helpers.NACT
        nodeUtil = 0.0
        for i in range(0, helpers.NACT):
            nextHistory = history + ("p" if i == 0 else "b")
            if player == 0:
                util[i] = self.cfr(cards, nextHistory, p0 * strategy[i], p1)
            else:
                util[i] = self.cfr(cards, nextHistory, p0, p1 * strategy[i])
            nodeUtil += strategy[i] * util[i]

        for i in range(0, helpers.NACT):
            regret = util[i] - nodeUtil
            node.regretSum[i] += (p1 if player == 0 else p0) * regret
        return nodeUtil