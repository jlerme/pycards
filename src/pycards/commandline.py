'''
Created on 8 aout 2013

@author: ju
'''
from cmd import Cmd

class AdminCmd(Cmd):
    '''
    create a command line interpreter with admin command
    '''
    __server = None
    def __init__(self, server):
        '''
        Constructor
        '''
        Cmd.__init__(self)
        self.__server = server
    
    def do_players(self, params):
        '''
        Return the list of registered players
        '''
        print self.__server.players
    
    def do_start(self, params):
        '''
        Start the game
        '''
        self.__server.start_game()