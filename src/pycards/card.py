'''
Created on 4 aout 2013

@author: ju
'''
from UserDict import UserDict

class Card(UserDict):
    '''
    Represent a card with
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
        if self.hidden:
            return "A Card"
        else:
            return UserDict.__repr__(self)
    
    def hide(self, hidden=True):
        self.hidden = hidden
        
    def show(self):
        return UserDict.__repr__(self)
    