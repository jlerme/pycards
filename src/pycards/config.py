'''
Created on 17 aout 2013

@author: ju
'''
import ConfigParser
import logging

config  = ConfigParser.RawConfigParser()

logging.basicConfig(filename='server.log', filemode="w", level=logging.DEBUG)
logging.info("Loading the configuration")
config.read("pycards.cfg")