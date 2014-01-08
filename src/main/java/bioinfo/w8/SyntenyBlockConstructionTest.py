'''
Created on Jan 8, 2014

@author: grmsjac6
'''
import unittest
from BreakDistance import sharedKmers,assignment

class Test(unittest.TestCase):


    def testSharedKmers(self):
        
        s= 3
        v = "AAACTCATC"
        w = "TTTCAAATC"
    
        t = sharedKmers(s, v, w)
        print("\n".join([ "("+str(ti[0])+","+str(ti[1])+")" for ti in t]))
        tt=[(0, 4),(0, 0),(4, 2),(6, 6)]
        assert len(t)==len(tt)

    def testAssignment(self):
        assignment()
    
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testSBC']
    unittest.main()