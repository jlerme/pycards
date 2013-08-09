'''
Created on 8 aout 2013

@author: ju
'''
from threading import Thread
import Pyro4

class RegisterThread(Thread):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        Thread.__init__(self, name = self.__class__.__name__)
        print "Thread " + str(self.__class__.__name__) + " created"
        
        daemon=Pyro4.Daemon()
        ns=Pyro4.locateNS()
        uri=daemon.register(self)
        ns.register("pycards.register", uri)
        
        daemon.requestLoop()
        
    def register(self, name):
        print "TBD : Create player " + name
        
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
        
class adminThread(Thread):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        Thread.__init__(self, name = self.__class__.__name__)
        print "Thread " + str(self.__class__.__name__) + " created"
