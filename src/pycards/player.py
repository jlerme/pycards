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

    def __init__(self, name="John Doe", attributes=None):
        '''
        Create a new player
        '''
        UserDict.__init__(self)
        self.name = name
        self.update(attributes)
        self["hand"] = Deck(name="Hand of " + name)
        
    def __repr__(self):
        return self.name
    
    def getHand(self):
        return self["hand"]
        
    def getAttributes(self, attributes=None):
        if attributes:
            return dict(zip(attributes,map(lambda x : self.data[x], attributes)))
        else:
            return self.data
    
    def playCard(self,index):
        return self["hand"].pop(index)