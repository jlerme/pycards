'''
Created on 8 aout 2013

@author: ju
'''
from threading import Thread
        
class GameThread(Thread):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        Thread.__init__(self, name = self.__class__.__name__)
        print "Thread " + str(self.__class__.__name__) + " created"

class ChatThread(Thread):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        Thread.__init__(self, name = self.__class__.__name__)
        print "Thread " + str(self.__class__.__name__) + " created"