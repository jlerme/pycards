'''
Created on 20 juil. 2013

@author: ju
'''
from pycards.deck import Deck
import ConfigParser
import importlib
from pycards.player import Player

config = ConfigParser.RawConfigParser()

def createDeck():
    loaderName=config.get("Modules", "deck.loader")
    loader=importlib.import_module(loaderName)
    deck = Deck()
    deck.data = loader.createDeck(config.get("Files","deck.filename"))
    deck.shuffle()
    return deck

def createPlayers():
    players=list()
    for (k,v) in config.items("Players"):
        players.append(Player(v))
    return players

if __name__ == '__main__':
    config.read("pycards.cfg")

    deck = createDeck()
    graveyard = Deck(name="Graveyard")
    
    players = createPlayers()
    print players