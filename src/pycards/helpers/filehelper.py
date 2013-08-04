'''
Created on 4 aout 2013
Allow to create card from a file with specific syntax
Syntax TBD
@author: ju
'''
from pycards import card
import re

regexp = re.compile("(\d+) (\w+)")

def createDeck(filename="deck.dat"):
    '''Check if the file exist and launch the parsing'''
    myFile = None
    try:
        myFile = open(filename, "r")
        lines = myFile.readlines()
        cardList = [ __parse(line) for line in lines ]
        print cardList
        return cardList
    except IOError, e:
        print e
    finally:
        if myFile:
            myFile.close()

def __parse(line):
    '''Create a card deck and return it'''
    lineTuple = regexp.search(line).groups()
    return card.BasicCard(lineTuple[0], lineTuple[1])
    
        
