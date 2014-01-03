'''
Created on Jan 3, 2014

@author: giannis
'''
import unittest
from LinearSpaceAllignment import linearSpaceAllignment
from bioinfo.w6.Allignment import globalAlign
class Test(unittest.TestCase):


    def testLinearSpaceAllignment(self):
        v="PLEASANTLY"
        w="MEANLY"

        st = 8
        vt = "PLEASANTLY"
        wt = "-MEA--N-LY"
        
        s,vv,ww = globalAlign(v, w)
        
        assert s == st
        assert vv==vt
        assert ww == wt

    def testAssignment(self):
        f = open('dataset_78_8.txt')
        v = next(f).strip()
        w = next(f).strip()
            
        s,vv,ww = globalAlign(v, w)
        
        print(s)
        print(vv)
        print(ww)
        
        
        pass
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()