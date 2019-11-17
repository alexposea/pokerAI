import random
from tkinter import PhotoImage

PASS = 0
BET = 1
NACT = 2

def getCards():
    cards = []
    arr = [None] * 14
    for i in range(1, 14):
        arr[i] = PhotoImage(file = "../cards/C" + str(i) + ".gif")
    cards.append(arr)
    arr = [None] * 14
    for i in range(1, 14):
        arr[i] = PhotoImage(file = "../cards/D" + str(i) + ".gif")
    cards.append(arr)
    arr = [None] * 14
    for i in range(1, 14):
        arr[i] = PhotoImage(file = "../cards/H" + str(i) + ".gif")
    cards.append(arr)
    arr = [None] * 14
    for i in range(1, 14):
        arr[i] = PhotoImage(file = "../cards/S" + str(i) + ".gif")
    cards.append(arr)
    arr = []
    arr.append(PhotoImage(file = "../cards/B.gif"))
    cards.append(arr)
    return cards

def buildDeck():
    cards = []
    for suit in ["S", "H", "D", "C"]:
        for card in range(1, 14):
            cards.append(str(card) + suit)
    return cards

def shuffleDeck():
    cards = buildDeck()
    for i in range(51, -1, -1):
        j = random.randint(0, i)
        cards[i], cards[j] = cards[j], cards[i]

def shuffle(c):
    cards = c
    for i in [2, 1]:
        j = random.randint(0, i)
        c[i], c[j] = c[j], c[i]
    return c