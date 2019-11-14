import helpers

class Node:
    def __init__(self, infoSet = ""):
        self.infoSet = infoSet
        self.regretSum = [0.0] * helpers.NACT
        self.strategy = [0.0] * helpers.NACT
        self.strategySum = [0.0] * helpers.NACT

    def getStrategy(self, realizationWeight):
        normalizingSum = 0.0
        for i in range(0, helpers.NACT):
            self.strategy[i] = max(self.regretSum[i], 0.0)
            normalizingSum += self.strategy[i]
        for i in range(0, helpers.NACT):
            if normalizingSum > 0:
                self.strategy[i] /= normalizingSum
            else:
                self.strategy[i] = 1.0 / helpers.NACT
            self.strategySum[i] += realizationWeight * self.strategy[i]
        return self.strategy

    def getAverageStrategy(self):
        avgStrat = [0.0] * helpers.NACT
        normalizingSum = 0.0
        for i in range(0, helpers.NACT):
            normalizingSum += self.strategySum[i]
        for i in range(0, helpers.NACT):
            if normalizingSum > 0:
                avgStrat[i] = self.strategySum[i] / normalizingSum
            else:
                avgStrat[i] = 1.0 / helpers.NACT
        return avgStrat

    def __str__(self):
        return self.infoSet + ": " + str(self.getAverageStrategy())