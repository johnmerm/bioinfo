'''
Created on Dec 11, 2013

@author: grmsjac6
'''
import unittest
from DCPChange import manhattanTourist

class Test(unittest.TestCase):


    def testManhattan(self):
        n=4
        m=4
        down=[[1,0,2,4,3],
              [4,6,5,2,1],
              [4,4,5,2,1],
              [5,6,8,5,3]]
        
        right=[[3,2,4,0],
               [3,2,4,2],
               [0,7,3,3],
               [3,3,0,2],
               [1,3,2,2]]
        
        mh = manhattanTourist(n, m, down, right)
        
        assert mh == 34



if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testManhattan']
    unittest.main()