'''
Created on 9 aout 2013

@author: ju
'''
import Pyro4
from pycards.player import Player

class Client(object):
    
    _player = None
    _server = None
    
    def __init__(self, name):
        self._server = Pyro4.Proxy("PYRONAME:pycards.server")
        self._player = self._server.register(name)
        print self.player

if __name__ == '__main__':
    name = raw_input("What is your name ?\n")
    Client(name)