'''
Created on Jan 6, 2014

@author: giannis
'''
import unittest
from MultipleLCS import threeSequences

class Test(unittest.TestCase):


    def testMultipleLCS(self):
        
        
        v=['ATATCCG',
           'TCCGA',
           'ATGTACTG']
         
        st = 3
        vt=['ATATCC-G-',
            '---TCC-GA',
            'ATGTACTG-']
        s,vv = threeSequences(v)
        
        assert s == st
    def testAsignment(self):
        v=['AACCGTAACT',
           'GGCCCGGC',
           'CCGCGTTCGG']
        
        
        s,vv = threeSequences(v)
        
        print(s)
        print("\n".join(vv))
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()