import helpers
import Game
from tkinter import *

class Window(Frame):
    def __init__(self, master = None, title = "Poker"):
        Frame.__init__(self, master)
        self.master = master
        self.drawMainMenu()
        self.master.title = title
        self.place()
        self.cardSprites = helpers.getCards()

    def drawMainMenu(self):
        self.drawMenuBar()
        label = Label(self.master, text = "Welcome to Poker! Press File -> New Game")
        label.place(x = 0, y = 0)

    def initGame(self, type):
        if type == "Kuhn":
            self.game = Game.Game()
            self.drawKuhn("", True)
        elif type == "Texas":
            self.game = Texas.Texas()
            self.drawTexas()

    def drawKuhn(self, history ="", fst = False):
        for widget in self.master.winfo_children():
            if widget is not self:
                widget.destroy()
        self.drawMenuBar()

        if history[-1:] == "b":
            self.game.bet("h")

        infoText = ""
        end = ""

        if history[-2:] == "bp":
            infoText += "You Lost!\n"
            history = ""
            self.game.reset("Hfold")
            if self.game.player.getChips() == 0:
                end = "h"
            elif self.game.humanPlayer.getChips() == 0:
                end = "c"
        elif history[-2:] == "bb" or history[-2:] == "pp":
            win = self.game.reset("show")
            if self.game.player.getChips() == 0:
                end = "h"
            elif self.game.humanPlayer.getChips() == 0:
                end = "c"
            if win == "h":
                infoText += "You Won!\n"
                history = ""
            else:
                infoText += "You Lost!\n"
                history = ""

        if history == "":
            infoText += "New round, choose an action!\n"
            fst = True

        if not fst:
            act = self.game.player.nextAction(history)
            if act == "bet":
                self.game.bet()
                history += "b"
                infoText += "Your opponent bet!\n"
            else:
                history += "p"
                infoText += "Your opponent passed!\n"

            if history[-2:] == "bp":
                infoText += "You Won!\n"
                infoText += "New round, choose an action!\n"
                history = ""
                self.game.reset("AIfold")
                if self.game.player.getChips() == 0:
                    end = "h"
                elif self.game.humanPlayer.getChips() == 0:
                    end = "c"
            elif history[-2:] == "bb" or history[-2:] == "pp":
                win = self.game.reset("show")
                if self.game.player.getChips() == 0:
                    end = "h"
                elif self.game.humanPlayer.getChips() == 0:
                    end = "c"
                if win == "h":
                    infoText += "You Won!\n"
                    infoText += "New round, choose an action!\n"
                    history = ""
                else:
                    infoText += "You Lost!"
                    infoText += "New round, choose an action!\n"
                    history = ""
        if end == "":
            playerCard = self.game.humanPlayer.card

            infoLabel = Label(self.master, text = infoText);
            infoLabel.place(x = 10, y = 10)
            cardLabel = Label(self.master, image = self.cardSprites[3][playerCard])
            cardLabel.place(x = 137, y = 82)
            chipLabel = Label(self.master, text = "You have " + str(self.game.humanPlayer.getChips()) + " chips. Your opponent has " + str(self.game.player.getChips()) + " chips")
            chipLabel.place(x = 10, y = 150)
            potLabel = Label(self.master, text = "Pot: " + str(self.game.pot) + " chips")
            potLabel.place(x = 10, y = 165)

            betButton = Button(self.master, text = "BET", command = lambda: self.drawGame(history + "b", False))
            betButton.place(x = 10, y = 200)
            passButton = Button(self.master, text = "PASS", command = lambda: self.drawGame(history + "p", False))
            passButton.place(x = 100, y = 200)

        elif end == "h":
            infoLabel = Label(self.master, text="Game over, you won!");
            infoLabel.place(x=10, y=10)
        else:
            infoLabel = Label(self.master, text="Game over, you lost!");
            infoLabel.place(x=10, y=10)

    def drawTexas(self):
        for widget in self.master.winfo_children():
            if widget is not self:
                widget.destroy()
        self.drawMenuBar()

    def drawMenuBar(self):
        menuBar = Menu(self.master)
        self.master.config(menu = menuBar)
        file = Menu(menuBar, tearoff = 0)
        newgame = Menu(file, tearoff = 0)
        newgame.add_command(label = "1 CPU Kuhn", command = lambda: self.initGame("Kuhn"))
        newgame.add_command(label = "1 CPU Texas Hold'Em", command = lambda: self.initGame("Texas"))
        file.add_cascade(label = "New Game", menu = newgame)
        file.add_command(label = "Exit", command = self.exitGame)
        menuBar.add_cascade(label = "File", menu = file)

    def exitGame(self):
        exit()

root = Tk()
root.geometry("500x300")
app = Window(root)
root.mainloop()