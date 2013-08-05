'''
Created on 5 aout 2013

@author: ju
'''
from pycards.deck import Deck
from UserDict import UserDict

class Player(UserDict):
    '''
    Represent a player.
    A player has a name, an hand and zero or more attributes
    '''
    name = None
    hand = None

    def __init__(self, name="John Doe", attributes=None):
        '''
        Create a new player
        '''
        self.name = name
        self.hand = Deck(name="Hand of " + name)
        self.data = attributes
        
    def __repr__(self):
        return self.name
    
    def showHand(self):
        print self.hand
        
    def showAttributes(self, attributes=None):
        if attributes:
            print dict(zip(attributes,map(lambda x : self.data[x], attributes)))
        else:
            print self.data
    
    def playCard(self,index):
        return self.hand.pop(index)