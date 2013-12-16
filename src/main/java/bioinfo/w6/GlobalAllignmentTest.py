'''
Created on Dec 16, 2013

@author: grmsjac6
'''
import unittest
from Allignment import globalAlign
from bioinfo.w6.Allignment import allignDAG

class Test(unittest.TestCase):


    def testGlobalAllignment(self):
        v = "PLEASANTLY"
        w = "MEANLY"
        s,o,u = allignDAG(v,w,False)
        
        print(o)
        print(u)
        
        assert s == 8
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testGlobalAllignment']
    unittest.main()