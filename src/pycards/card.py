'''
Created on 4 aout 2013

@author: ju
'''
from UserDict import UserDict

class Card(UserDict):
    '''
    Represent a card
    A card has the default attributes : name, value and description
    '''
    hidden=False

    def __init__(self, value=0, name=None, description=None, hidden=False):
        '''
        Create a new card
        '''
        UserDict.__init__(self)
        self["name"] = name
        self["value"] = value
        self["description"] = description
        self.hidden = hidden 
        

    def __repr__(self):
        '''
        if the card is hidden, return "A card"
        otherwise return the true representation of the card
        '''
        if self.hidden:
            return "A Card"
        else:
            return UserDict.__repr__(self)
    
    def hide(self, hidden=True):
        '''
        Change the visibility of the card
        '''
        self.hidden = hidden
        
    def show(self):
        '''
        Show the card even if the visibility is set to hidden
        '''
        return UserDict.__repr__(self)
    