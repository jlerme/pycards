'''
Created on 15 aout 2013

@author: ju
'''

import unittest
from unittest.suite import TestSuite

if __name__ == '__main__':
    suite = TestSuite()
    loader = unittest.TestLoader()
    suite.addTests(loader.discover(start_dir="test", pattern="*test.py"))
    
    unittest.TextTestRunner(verbosity=1).run(suite)