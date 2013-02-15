import unittest

from conway.say import blocks

class testBlocks(unittest.TestCase):
    def testBlocksEmpty(self):
        self.assertEquals([], blocks(''))

    def testBlocks1(self):
        self.assertEquals(['1'], blocks('1'))

    def testBlocks11(self):
        self.assertEquals(['11'], blocks('11'))

    def testBlocks21(self):
        self.assertEquals(['2', '1'], blocks('21'))

    def testBlocks1211(self):
        self.assertEquals(['1', '2', '11'], blocks('1211'))

if __name__ == '__main__':
    unittest.main()
