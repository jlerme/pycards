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

global server

class Server(object):
    
    daemon  = Pyro4.Daemon()
    config  = ConfigParser.RawConfigParser()
    players = {}
    __single = None
    
    def __init__(self):
        if self.__single:
            raise self.__single
        self.__single = self
        
        logging.basicConfig(filename='server.log', filemode="w", level=logging.DEBUG)
        logging.info("Loading the configuration")
        self.config.read("pycards.cfg")
        
 
        logging.info("Registering server in the pyro NameServer")
        ns=Pyro4.locateNS()
        uri=self.daemon.register(self)
        ns.register("pycards.server", uri)
        
    def __createDeck(self):
        loaderName=self.config.get("Modules", "deck.loader")
        loader=importlib.import_module(loaderName)
        deck = Deck()
        deck.data = loader.createDeck(self.config.get("Files","deck.filename"))
        deck.shuffle()
        return deck
    
    def start(self):
        logging.info("Creating the decks")
        self.deck = self.__createDeck()
        self.graveyard = Deck(name="Graveyard")
    
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

def test():
    print "test"

if __name__ == '__main__':
    server = Server().start()