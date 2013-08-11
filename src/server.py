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
    daemon  = Pyro4.Daemon()
    config  = ConfigParser.RawConfigParser()
    players = {}
    __nameServer = None
    __gameThread = None
    
    def __init__(self):
        '''
        Constructor
        Load the configuration
        Initialise the logging service
        Register the server in the Pyro NameServer
        '''
        logging.basicConfig(filename='server.log', filemode="w", level=logging.DEBUG)
        logging.info("Loading the configuration")
        self.config.read("pycards.cfg")
        
 
        logging.info("Registering server in the pyro NameServer")
        self.__nameServer=Pyro4.locateNS()
        uri=self.daemon.register(self)
        self.__nameServer.register("pycards.server", uri)
        
    def __createDeck(self):
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
        Start Pyro daemon
        '''
        logging.info("Starting Chat thread")
        ChatThread()
        
        logging.info("Starting admin command line")
        adminThread = Thread(target=AdminCmd(self).cmdloop)
        adminThread.start()
        
        logging.info("Starting Pyro daemon")
        self.daemon.requestLoop()
        
    def register(self, name):
        logging.info("Creating player " + name)
        self.players[name] = Player(name)
    
    def start_game(self):
        '''
         Create initial decks for the game
         Start the game
        '''
        logging.info("Creating the decks")
        decks = self.__createDecks()
        
        self.__gameThread = GameThread(self.players.items(), decks)
        uri=self.daemon.register(self.__gameThread)
        self.__nameServer.register("pycards.game", uri)
        self.__gameThread.start()
        while True:
            time.sleep(10)
            self.__gameThread.play()

    def stop_game(self):
        self.__gameThread.stop()

if __name__ == '__main__':
    Server().start()