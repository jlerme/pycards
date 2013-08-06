'''
Created on 5 aout 2013

@author: ju
'''
import unittest
from pycards.card import Card


class cardTest(unittest.TestCase):

    def setUp(self):
        self.card = Card(1,"As")

    def testhide(self):
        self.assertEqual(self.card.__repr__(), "{'name': 'As', 'value': 1, 'description': None}")
        self.card.hide(True)
        self.assertEqual(self.card.__repr__(), "A Card")
        self.card.hide(False)
        self.assertEqual(self.card.__repr__(), "{'name': 'As', 'value': 1, 'description': None}")
        
    def testshow(self):
        self.assertEqual(self.card.get(), "{'name': 'As', 'value': 1, 'description': None}")
        self.card.hide(True)
        self.assertEqual(self.card.get(), "{'name': 'As', 'value': 1, 'description': None}")
        self.card.hide(False)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()