import unittest

from conway.test.say import testSay
from conway.test.blocks import testBlocks
from conway.test.convert import testConvert

class EvaluateSuite(unittest.TestSuite):
    def __init__(self):
        unittest.TestSuite.__init__(self)
        for clazz in [testSay, testBlocks, testConvert]:
            self.addTest(unittest.makeSuite(clazz))

if __name__ == '__main__':
    suite = EvaluateSuite()

    unittest.TextTestRunner().run(suite)
