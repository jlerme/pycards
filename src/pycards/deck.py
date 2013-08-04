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
        
    def draw(self):
        '''
        Draw a card in the deck
        '''
        return self.data.pop()
    
    