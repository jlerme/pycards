'''
Created on 8 aout 2013

@author: ju
'''
from threading import Thread
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
        
class AdminThread(Thread):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        Thread.__init__(self, name = self.__class__.__name__)
        print "Thread " + str(self.__class__.__name__) + " created"

    def run(self):
        AdminCmd().cmdloop(self)