'''
Created on 4 aout 2013

@author: ju
'''
from UserList import UserList
import random
import logging

class Deck(UserList):
    '''
    Represent a deck : list of cards
    '''
    name = ""

    def __init__(self, name="Default deck"):
        '''
        Create a deck
        '''
        UserList.__init__(self)
        self.name = name
        logging.info("Creating %s" % name)
        
    def shuffle(self):
        '''
        Shuffle the deck
        '''
        random.shuffle(self.data)
        
    def draw(self, number=1):
        '''
        Draw a card in the deck
        '''
        return [ self.data.pop() for _ in xrange(number)]
    
    def addCard(self, card, hidden=True, index=1):
        '''
        Add a card in the deck to the given index
        Its visibility can be changed (default : hidden)
        '''
        card.hide(hidden)
        self.data.insert(index-1, card)
        
    def getCard(self, index=1):
        '''
        Show the card at the given index
        Its visibility can be changed (default : hidden)
        '''
        card = self.data.__getitem__(index-1)
        return card.get()
        