'''
Created on 5 aout 2013

@author: ju
'''
from pycards.deck import Deck
from UserDict import UserDict
import Pyro4
import logging

class Player(UserDict):
    '''
    Represent a player.
    A player has a name, an hand and zero or more attributes
    '''

    def __init__(self, name=None, attributes=None):
        '''
        Create a new player
        '''
        UserDict.__init__(self)
        
        if name:
            self["name"] = name
            self["waiting"]=True
            self["hand"] = Deck(name="Hand of " + name)
 
        self.update(attributes)
    
    def __repr__(self):
        return self.data["name"]
    
    def getHand(self):
        return self["hand"]
        
    def getAttributes(self, attributes=None):
        if attributes:
            return dict(zip(attributes,map(lambda x : self.data[x], attributes)))
        else:
            return self.data
    
    def playCard(self,index):
        return self["hand"].pop(index)
    
    @staticmethod
    def unserialize(data):
        logging.debug("unserialize " + str(data))
        data = data["data"]
        data["hand"] = Deck.unserialize(data["hand"])
        return Player(attributes=data)