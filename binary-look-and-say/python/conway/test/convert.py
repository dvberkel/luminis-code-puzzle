import unittest

from conway.say import convert

class testConvert(unittest.TestCase):
    def testConvert1base10(self):
        self.assertEquals('1', convert(1,10))

    def testConvert12base10(self):
        self.assertEquals('12', convert(12,10))

    def testConvert123base10(self):
        self.assertEquals('123', convert(123,10))

    def testConvert1base2(self):
        self.assertEquals('1', convert(1,2))

    def testConvert2base2(self):
        self.assertEquals('10', convert(2,2))

    def testConvert5base2(self):
        self.assertEquals('101', convert(5,2))

if __name__ == '__main__':
    unittest.main()
