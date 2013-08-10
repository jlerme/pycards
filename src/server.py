'''
Created on 20 juil. 2013

@author: ju
'''
from pycards.deck import Deck
import ConfigParser
import importlib
from pycards.player import Player
from pycards.server.thread import ChatThread, GameThread, AdminThread
import Pyro4


class Server(object):
    
    daemon=Pyro4.Daemon()
    config = ConfigParser.RawConfigParser()

    def __init__(self):
        self.config.read("pycards.cfg")
 
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
        self.deck = self.__createDeck()
        self.graveyard = Deck(name="Graveyard")
    
        self.chatThread = ChatThread()
        self.commandline = AdminThread()
        
        self.commandline.start()
        self.daemon.requestLoop()
        
    def register(self, name):
        print "TBD : Create player " + name

if __name__ == '__main__':
    Server().start()