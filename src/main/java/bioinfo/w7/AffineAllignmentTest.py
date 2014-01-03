'''
Created on Jan 3, 2014

@author: giannis
'''
import unittest
from AffineAlignment import affineAllign

class Test(unittest.TestCase):


    def testAffine(self):
        v="PRTEINS"
        w="PRTWPSEIN"


        st = 8
        vt = "PRT---EINS"
        wt = "PRTWPSEIN-"
        s,vv,ww = affineAllign(v, w)
        
        assert s == st
        assert vv == vt
        assert ww == wt


    def testAssignment(self):
        f = open('dataset_78_8.txt')
        v = next(f).strip()
        w = next(f).strip()
        
        s,vv,ww = affineAllign(v, w)
        
        print(s)
        print(vv)
        print(ww)
        
        pass
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testAffine']
    unittest.main()