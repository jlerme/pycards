'''
Created on 4 aout 2013
Allow to create card from a file with specific syntax
Syntax TBD
@author: ju
'''
from pycards import card
import logging

def createDeck(filename="deck.dat"):
    '''Check if the file exist and launch the parsing'''
    logging.info("Loading " + filename + " file")
    
    with open(filename, "r") as myFile: 
        lines = myFile.readlines()
        attributes = lines.pop(0).split()
        cardList = [ __parse(line, attributes) for line in lines ]
        return cardList

def __parse(line, attributes):
    '''Create a card deck and return it'''
    aTuple = line.split()
    aCard = card.Card()
    aCard.data = dict(zip(attributes, aTuple))
    logging.debug("Creating card " + aCard.__repr__())
    return aCard
    
        
