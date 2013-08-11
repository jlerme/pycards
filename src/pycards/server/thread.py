'''
Created on 8 aout 2013

@author: ju
'''
import threading
import logging
        
class GameThread(threading.Thread):
    '''
    classdocs
    '''
    __players = []
    __decks = {}
    __lock = threading.Lock()
    __playerTurn = None

    def __init__(self, players, decks):
        '''
        Constructor
        '''
        threading.Thread.__init__(self, name = self.__class__.__name__)
        logging.info( "Thread " + str(self.__class__.__name__) + " created")
        self.__players = players
        self.__decks = decks

    def run(self):
        while True:
            for player in self.__players:
                print "Wait for " + player.name + " to play"
                self.__playerTurn = player
                self.__lock.acquire()
                
    def endOfTurn(self):
        self.__lock.release()
        
    def draw(self, player, deck="Main", number="1"):
        cards = self.__decks[deck].draw(number)
        for card in cards:
            self.__players[player].getHand().addCard(card)
        return cards
    
    def discard(self, player, card, deck="Graveyard"):
        self.__players[player].getHand().remove(card)
        self.__decks[deck].addCard(card,hidden=False)
        
    def play(self, player, card):
        print "Player " + player + " shows " + card.show()
        
    def show(self, player, deck, number=1):
        if number == 0:
            for card in self.__decks[deck]:
                card.show()
        else:
            for x in xrange(number):
                self.__decks[deck].getCard(x).show()
        
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