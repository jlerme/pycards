'''
Created on 20 juil. 2013

@author: ju
'''
from pycards.deck import Deck
import ConfigParser
import importlib
from pycards.player import Player
from pycards.server.thread import ChatThread, GameThread
import Pyro4
import logging
from threading import Thread
from pycards.commandline import AdminCmd
import time

global server

class Server(object):
    '''
    Main thread
    Load the configuration and all threads
    Register players
    Configure and start all Pyro stuff
    '''
    config  = ConfigParser.RawConfigParser()
    players = {}
    _nameServer = None
    _gameThread = None
    
    def __init__(self):
        '''
        Constructor
        Load the configuration
        Initialise the logging service
        '''
        logging.basicConfig(filename='server.log', filemode="w", level=logging.DEBUG)
        logging.info("Loading the configuration")
        self.config.read("pycards.cfg")      
        
    def _createDeck(self):
        '''
        Create initial deck
        Get the loader according to the configuration and load the deck
        Then shuffle it
        '''
        loaderName=self.config.get("Modules", "deck.loader")
        loader=importlib.import_module(loaderName)
        deck = Deck()
        deck.data = loader.createDeck(self.config.get("Files","deck.filename"))
        deck.shuffle()
        
        decks = dict()
        decks["Main"] = deck
        decks["Graveyard"] = Deck("Graveyard")
        
        return decks
    
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
            self._nameServer=Pyro4.locateNS()
            uri=daemon.register(ServerAdapter(self))
            self._nameServer.register("pycards.server", uri)
            
            logging.info("Starting Pyro daemon")
            daemon.requestLoop()
        
    def register(self, name):
        logging.info("Creating player " + name)
        self.players[name] = Player(name)
        return self.players[name]
    
    def start_game(self):
        '''
         Create initial decks for the game
         Start the game
        '''
        logging.info("Creating the decks")
        decks = self.__createDecks()
        
        self._gameThread = GameThread(self.players.items(), decks)
        uri=self._pyroDaemon.register(self._gameThread)
        self._nameServer.register("pycards.game", uri)
        self._gameThread.start()

    def stop_game(self):
        self._gameThread.stop()

class ServerAdapter(object):
    """ Adapter for the server to use in the pyro service """
    
    _server = None
    _exportedMethods = [ "register" ]
    
    def __init__(self, server):
        self._server = server
        
    def __getattr__(self, attr):
        """Everything else is delegated to the object"""
        if attr in self._exportedMethods:
            return getattr(self._server, attr)
        else:
            raise NotImplementedError

if __name__ == '__main__':
    Server().start()