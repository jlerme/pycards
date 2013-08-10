'''
Created on 8 aout 2013

@author: ju
'''
from threading import Thread
import logging
from pycards.commandline import AdminCmd
        
class GameThread(Thread):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        Thread.__init__(self, name = self.__class__.__name__)
        logging.info( "Thread " + str(self.__class__.__name__) + " created")

class ChatThread(Thread):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        Thread.__init__(self, name = self.__class__.__name__)
        logging.info("Thread " + str(self.__class__.__name__) + " created")