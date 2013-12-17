'''
Created on Dec 16, 2013

@author: grmsjac6
'''
import unittest


from Allignment import localAlign

class Test(unittest.TestCase):


    def testLocalAlignment(self):
        v = "MEANLY"
        w = "PENALTY"
        
        s,vv,ww = localAlign(v, w) 
        
        assert s == 15
        assert vv == "EANL-Y"
        assert ww == "ENALTY"


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testLocalAllignment']
    unittest.main()