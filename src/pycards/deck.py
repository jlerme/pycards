'''
Created on 4 aout 2013

@author: ju
'''
from UserList import UserList
import random

class Deck(UserList):
    '''
    Represent a deck : list of cards
    '''
    name = ""

    def __init__(self, name="Default"):
        '''
        Create a deck
        '''
        UserList.__init__(self)
        self.name = name
        print "Create %s deck" % name
        
    def shuffle(self):
        '''
        Shuffle the deck
        '''
        random.shuffle(self.data)
        
    def draw(self, number=1):
        '''
        Draw a card in the deck
        '''
        return [ self.data.pop() for i in xrange(number)]
    
    def addCard(self, card, hidden=True, index=1):
        card.hide(hidden)
        self.data.insert(index-1, card)
        
    def showCard(self, hidden=True, index=1):
        card = self.data.__getitem__(index-1)
        print card.show()
        card.hide(hidden)
        