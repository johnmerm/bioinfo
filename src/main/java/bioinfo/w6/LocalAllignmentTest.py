'''
Created on Dec 16, 2013

@author: grmsjac6
'''
import unittest

from Allignment import allignDAG

class Test(unittest.TestCase):


    def testLocalAllignment(self):
        v = "MEANLY"
        w = "PENALTY"
        
        s,vv,ww = allignDAG(v, w, True) 
        
        assert s == 15
        assert vv == "EANL-Y"
        assert ww == "ENALTY"


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testLocalAllignment']
    unittest.main()