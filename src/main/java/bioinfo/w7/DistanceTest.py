'''
Created on Dec 20, 2013

@author: giannis
'''
import unittest
from Distance import distance

class Test(unittest.TestCase):


    def testDistance(self):
        v="PLEASANTLY"
        w="MEANLY"
        d,vv,ww = distance(v, w)
        print(vv)
        print(ww)
        assert d == 5

    def testFittingDistance(self):
        v="TAGGCTTA"
        w="TAGATA"
        d,vv,ww = distance(v, w)
        print(vv)
        print(ww)
        assert d == 5
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testDistance']
    unittest.main()