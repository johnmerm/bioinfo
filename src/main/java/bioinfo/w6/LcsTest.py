'''
Created on Dec 13, 2013

@author: grmsjac6
'''
import unittest
from LCS import lcs

class Test(unittest.TestCase):


    def testLCS(self):
        v = "AACCTTGG"
        w = "ACACTGTGA"
        
        s,b,ret = lcs(v, w)
        out = "AACTGG"
        
        assert  len(ret) == len(out)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testLCS']
    unittest.main()
    
    
#AACCTTGG
#ACACTGTGA