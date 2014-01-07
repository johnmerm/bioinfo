'''
Created on Jan 7, 2014

@author: grmsjac6
'''
import unittest
from GreedyReversalSorting import greedySort,breakPointCount

class Test(unittest.TestCase):


    def testGreedySort(self):
        p = [-3,+4,+1,+5,-2]
        pp = greedySort(p)
        
        for pt in pp:
            print("(" + " ".join(["%+d" % i for i in pt]) + ")")
        
        assert len(pp) == 7
        

    def testBreakPointCnt(self):
        p=[+3,+4,+5,-12,-8,-7,-6,+1,+2,+10,+9,-11,+13,+14]
        b = breakPointCount(p)
        
        assert b == 8
        
    
       
    
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testGreedySort']
    unittest.main()