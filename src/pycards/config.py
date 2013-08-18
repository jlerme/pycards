'''
Created on 17 aout 2013

@author: ju
'''
import ConfigParser
import logging

LOG_SETTINGS = {
    'version': 1,
    'root': {
        'level': 'DEBUG',
        'handlers': ['console', 'file'],
    },
    'loggers': {
        'Pyro4.naming': {
            'handlers':['console'],
            'propagate': False,
            'level':'DEBUG',
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'level': 'INFO',
            'formatter': 'detailed',
            'stream': 'ext://sys.stdout',
        },
        'file': {
            'class': 'logging.handlers.RotatingFileHandler',
            'level': 'INFO',
            'formatter': 'detailed',
            'filename': 'pycards.log',
#            'mode': 'a',
            'maxBytes': 10485760,
            'backupCount': 5,
        },
    },
    'formatters': {
        'detailed': {
            'format': '%(asctime)s %(module)-17s line:%(lineno)-4d ' \
            '%(levelname)-8s %(message)s',
        },
    },
}

config  = ConfigParser.RawConfigParser()
logging.info("Loading the configuration")
config.read("pycards.cfg")