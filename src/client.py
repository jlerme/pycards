'''
Created on 9 aout 2013

@author: ju
'''
import Pyro4

if __name__ == '__main__':
    name = raw_input("What is your name ?")
    
    server = Pyro4.Proxy("PYRONAME:pycards.server")
    server.register(name)