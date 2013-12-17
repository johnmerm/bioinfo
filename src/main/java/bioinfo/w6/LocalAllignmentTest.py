'''
Created on Dec 16, 2013

@author: grmsjac6
'''
import unittest

from Allignment import allignDAG
from bioinfo.w6.Allignment import localAllign

class Test(unittest.TestCase):


    def testLocalAllignment(self):
        v = "MEANLY"
        w = "PENALTY"
        
        s,vv,ww = localAllign(v, w) 
        
        assert s == 15
        assert vv == "EANL-Y"
        assert ww == "ENALTY"


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testLocalAllignment']
    unittest.main()