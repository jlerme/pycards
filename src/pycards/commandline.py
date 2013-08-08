'''
Created on 8 aout 2013

@author: ju
'''
from cmd import Cmd

class AdminCmd(Cmd):
    '''
    create a command line interpreter with admin command
    '''


    def __init__(self):
        '''
        Constructor
        '''
        Cmd.__init__(self)
        