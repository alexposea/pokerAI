class Action():
    def __init__(self, type, amount = 1):
        self.type = type
        self.amount = 0
        if type is not "pass":
            self.amount = amount

    def getType(self):
        return self.type

    def getAmount(self):
        return self.amount

    def getAction(self):
        return (self.type, self.amount)