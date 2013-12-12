'''
Created on Dec 11, 2013

@author: grmsjac6
'''
import unittest
from DCPChange import  dcpChange

class Test(unittest.TestCase):


    def testDCPChange(self):
        money=40
        coins = [50,25,20,10,5,1]
        
        #money=19934
        #coins=[22,31,9,5,3,1]

        
        dcp = dcpChange(money, coins)
        print(dcp)
        assert dcp == 2


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testDCPChange']
    unittest.main()