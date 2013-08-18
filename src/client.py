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
        Pyro4.config.reset()
        Pyro4.config.SERIALIZER = 'json'
        Pyro4.util.SerializerBase.register_dict_to_class(Player, Player.unserialize)
        self._server = Pyro4.Proxy("PYRONAME:pycards.server")
        self._player = self._server.register(name)
        print self._player

if __name__ == '__main__':
    name = raw_input("What is your name ?\n")
    Client(name)