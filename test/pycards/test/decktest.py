'''
Created on 6 aout 2013

@author: ju
'''
import unittest
from pycards.deck import Deck
from pycards.loaders import fileloader
import copy
from pycards.card import Card


class Test(unittest.TestCase):


    def setUp(self):
        self.deck = Deck()
        self.deck.data = fileloader.createDeck()


    def tearDown(self):
        pass


    def testShuffle(self):
        initdeck=copy.deepcopy(self.deck)
        self.deck.shuffle()
        self.assertNotEqual(self.deck, initdeck)

    def testdraw(self):
        numberOfCards = len(self.deck)
        self.deck.draw()
        self.assertEqual(len(self.deck), numberOfCards - 1)
        numberOfCards = numberOfCards - 1
        self.deck.draw(5)
        self.assertEqual(len(self.deck), numberOfCards - 5)
        
    def testaddCard(self):
        testdeck = Deck()
        card = Card(1,"As")
        testdeck.addCard(card)
        self.assertEqual(testdeck.__repr__(), "[A Card]")
        card = Card(2,"Deux")
        testdeck.addCard(card,False)
        self.assertEqual(testdeck.__repr__(), "[{'name': 'Deux', 'value': 2, 'description': None}, A Card]")
        card = Card(3,"Trois")
        testdeck.addCard(card,False,2)
        self.assertEqual(testdeck.__repr__(), "[{'name': 'Deux', 'value': 2, 'description': None}, {'name': 'Trois', 'value': 3, 'description': None}, A Card]")

    def testshowCard(self):
        self.assertEqual(self.deck.getCard(), "{'color': 'Coeur', 'name': 'As', 'value': '1'}") 
        self.assertEqual(self.deck.getCard(7), "{'color': 'Coeur', 'name': 'Sept', 'value': '7'}") 
        
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()