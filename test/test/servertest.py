'''
Created on 15 aout 2013

@author: ju
'''
import unittest
from server import Server, ServerAdapter


class Test(unittest.TestCase):

    _server = None
    _serverAdapter = None

    def setUp(self):
        self._server = Server()
        self._serverAdapter = ServerAdapter(self._server)

    def tearDown(self):
        pass


    def testServer(self):
        self.assertIsNotNone(self._server.config.get("Modules", "deck.loader"))
        self.assertDictEqual(self._server.players, {}) 
        
    def testServerAdapter(self):
        self.assertIsNotNone(self._serverAdapter.register("Maka"))
        with self.assertRaises(NotImplementedError):
            self._serverAdapter.start()
        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()