'''
Created on 6 aout 2013

@author: ju
'''
import unittest
from pycards.player import Player


class Test(unittest.TestCase):


    def setUp(self):
        self.player=Player(attributes={"coin": 2, "team": "red"})


    def tearDown(self):
        pass


    def testgetAttributes(self):
        pass


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()