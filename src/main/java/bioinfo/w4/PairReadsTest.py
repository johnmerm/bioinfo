'''
Created on Dec 9, 2013

@author: grmsjac6
'''
import unittest
from PairedReads import pairedReads


class Test(unittest.TestCase):


    def testPairs(self):
        d = 2
        lines = ["GAGA|TTGA",
                 "TCGT|GATG",
                 "CGTG|ATGT",
                 "TGGT|TGAG",
                 "GTGA|TGTT",
                 "GTGG|GTGA",
                 "TGAG|GTTG",
                 "GGTC|GAGA",
                 "GTCG|AGAT"]
        
        string = pairedReads(lines,d)
        assert string == "GTGGTCGTGAGATGTTGA"
        pass


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()