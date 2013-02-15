import unittest

from conway.say import Sayer

class testSay(unittest.TestCase):
    def setUp(self):
        self.sayer = Sayer()

    def testSay1(self):
        self.assertEquals('11', self.sayer.say('1'))

    def testSay11(self):
        self.assertEquals('21', self.sayer.say('11'))

    def testSay21(self):
        self.assertEquals('1211', self.sayer.say('21'))

if __name__ == '__main__':
    unittest.main()
