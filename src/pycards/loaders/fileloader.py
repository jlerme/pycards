'''
Created on 4 aout 2013
Allow to create card from a file with specific syntax
Syntax TBD
@author: ju
'''
from pycards import card

def createDeck(filename="deck.dat"):
    '''Check if the file exist and launch the parsing'''
    myFile = None
    try:
        myFile = open(filename, "r")
        lines = myFile.readlines()
        attributes = lines.pop(0).split()
        cardList = [ __parse(line, attributes) for line in lines ]
        return cardList
    except IOError, e:
        print e
    finally:
        if myFile:
            myFile.close()

def __parse(line, attributes):
    '''Create a card deck and return it'''
    aTuple = line.split()
    aCard = card.Card()
    aCard.data = dict(zip(attributes, aTuple))
    return aCard
    
        
