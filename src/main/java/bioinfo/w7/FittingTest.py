'''
Created on Dec 20, 2013

@author: giannis
'''
import unittest
from Distance import fitting,assignment
class Test(unittest.TestCase):


    def testFitting(self):
        v="GTAGGCTTAAGGTTA"
        w= "TAGATA"
        
        s,vv,ww = fitting(v, w)
        sc = 0
        for i in range(len(vv)):
            if vv[i] == ww[i]:
                sc+=1
            else:
                sc -=1
        
        assert sc == s
        assert s == 2
      
      
    def testAssignment(self):
        s,vv,ww = assignment()
        n = len(vv)
        m = len(ww)
        
        assert n == m
        sc = 0
        for i in range(len(vv)):
            if vv[i] == ww[i]:
                sc+=1
            else:
                sc -=1
        
        assert sc == s


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testFitting']
    unittest.main()