'''
Created on 20 juil. 2013

@author: ju
'''
from pycards.deck import Deck
import ConfigParser
import importlib

config = ConfigParser.RawConfigParser()

if __name__ == '__main__':
    config.read("pycards.cfg")
    loaderName=config.get("Modules", "deck.loader")
    loader=importlib.import_module(loaderName)
    deck = Deck()
    deck.data = loader.createDeck(config.get("Files","deck.filename"))
    deck.shuffle()
    print deck
    card = deck.draw()
    print card
    print deck
    card.hide()
    print card
    card.hide(False)
    print card