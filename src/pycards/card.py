'''
Created on 4 aout 2013

@author: ju
'''
from UserDict import UserDict

class BasicCard(UserDict):
    '''
    Represent a card
    '''


    def __init__(self, value=0, name=None):
        '''
        Create a new card
        '''
        UserDict.__init__(self)
        self["name"] = name
        self["value"] = value
        

        