'''
Created on 20 juil. 2013

@author: ju
'''
from pycards.deck import Deck
from pycards.helpers import filehelper

if __name__ == '__main__':
    deck = Deck()
    deck.data = filehelper.createDeck()
    deck.shuffle()
    print deck
    card = deck.draw()
    print card
    print deck
    card.hide()
    print card
    card.hide(False)
    print card