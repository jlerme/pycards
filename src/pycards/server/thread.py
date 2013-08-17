'''
Created on 8 aout 2013

@author: ju
'''
import threading
import logging
from pycards.deck import Deck
import pycards.config as configuration
import importlib
        
class GameThread(threading.Thread):
    '''
    classdocs
    '''
    _players = []
    _decks = {}
    _lock = threading.Lock()
    _playerTurn = None

    def __init__(self, players):
        '''
        Constructor
        '''
        threading.Thread.__init__(self, name = self.__class__.__name__)
        logging.info( "Thread " + str(self.__class__.__name__) + " created")
        self._players = players

        loaderName=configuration.config.get("Modules", "deck.loader")
        logging.info("Importing deck loader " + loaderName)
        loader=importlib.import_module(loaderName)

        deck = Deck()
        deck.data = loader.createDeck(configuration.config.get("Files","deck.filename"))
        deck.shuffle()
        
        self._decks["Main"] = deck
        self._decks["Graveyard"] = Deck("Graveyard")


    def run(self):
        while True:
            for player in self._players:
                print "Wait for " + player.name + " to play"
                self._playerTurn = player
                self._lock.acquire()
                
    def endOfTurn(self):
        self._lock.release()
        
    def draw(self, player, deck="Main", number="1"):
        cards = self._decks[deck].draw(number)
        for card in cards:
            self._players[player].getHand().addCard(card)
        return cards
    
    def discard(self, player, card, deck="Graveyard"):
        self._players[player].getHand().remove(card)
        self._decks[deck].addCard(card,hidden=False)
        
    def play(self, player, card):
        print "Player " + player + " shows " + card.show()
        
    def show(self, player, deck, number=1):
        if number == 0:
            for card in self._decks[deck]:
                card.show()
        else:
            for x in xrange(number):
                self._decks[deck].getCard(x).show()
        
class ChatThread(threading.Thread):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        threading.Thread.__init__(self, name = self.__class__.__name__)
        logging.info("Thread " + str(self.__class__.__name__) + " created")