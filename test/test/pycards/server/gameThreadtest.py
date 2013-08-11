'''
Created on 11 aout 2013

@author: ju
'''
import unittest
from pycards.player import Player
from pycards.server.thread import GameThread
import time
from pycards.deck import Deck
from pycards.loaders import fileloader


class Test(unittest.TestCase):

    players = []
    decks = {}

    def setUp(self):
        self.decks["Main"] = Deck()
        self.decks["Main"].data = fileloader.createDeck()
        self.decks["Graveyard"] = Deck("Graveyard")
        self.players.append(Player("Maka"))
        self.players.append(Player("Makb"))
        self.players.append(Player("Makc"))


    def tearDown(self):
        pass


    def testEndOfTurn(self):
        game = GameThread(self.players, self.decks)
        game.setDaemon(True)
        game.start()
        for _ in xrange(5):
            time.sleep(2)
            game.endOfTurn()

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()