'''
Created on 20 juil. 2013

@author: ju
'''
from pycards.player import Player
from pycards.server.thread import ChatThread, GameThread
import Pyro4
import logging.config
from threading import Thread
from pycards.commandline import AdminCmd
from pycards.config import LOG_SETTINGS

class Server(object):
    '''
    Main thread
    Load all threads
    Register players
    Configure and start all Pyro stuff
    '''
    players = {}
    _gameThread = None
    
    def __init__(self):
        '''
        Constructor
        Nothing to do yet
        '''
        Pyro4.config.reset()
        Pyro4.config.SERIALIZER = 'json'
        Pyro4.util.SerializerBase.register_dict_to_class(Player, Player.unserialize)
        Thread(target=Pyro4.naming.startNSloop).start()
    
    def start(self):
        '''
        Start the server
        Start Chat thread
        Start an admin command line thread
        Register the server in the Pyro NameServer
        Start Pyro daemon
        '''
        logging.info("Starting Chat thread")
        ChatThread()
        
        logging.info("Starting admin command line")
        adminThread = Thread(target=AdminCmd(self).cmdloop)
        adminThread.start()
        
        logging.info("Registering the ServerAdapter in the pyro NameServer")
        with Pyro4.Daemon() as daemon:
            with Pyro4.locateNS() as nameServer:
                uri=daemon.register(ServerAdapter(self))
                nameServer.register("pycards.server", uri)
            
                logging.info("Starting Pyro daemon")
                daemon.requestLoop()
        
    def register(self, name):
        """ Register a player in the server"""
        logging.info("Creating player " + name)
        self.players[name] = Player(name)
        return self.players[name]
    
    def start_game(self):
        '''
         Start the game
        '''
        self._gameThread = GameThread(self.players.items())
        self._gameThread.start()

    def stop_game(self):
        self._gameThread.stop()

class ServerAdapter(object):
    """ Adapter for the server to use in the pyro service """
    
    _server = None
    _exportedMethods = [ "register" ]
    
    def __init__(self, server):
        self._server = server
    
    def draw(self, player, deck="Main", number="1"):
        self._server._gameThread.draw(player,deck,number)
        
    def __getattr__(self, attr):
        """Everything tagged as exported is delegated to the object"""
        if attr in self._exportedMethods:
            return getattr(self._server, attr)
        else:
            raise NotImplementedError

if __name__ == '__main__':
    logging.config.dictConfig(LOG_SETTINGS)
    Server().start()