'''
Created on Dec 9, 2013

@author: grmsjac6
'''
import unittest
from PairedReads import pairedReads
from bioinfo.w4.PairedReads import assignment


class Test(unittest.TestCase):
    def testAssign(self):
        assignment()

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

    def testExtraDataSet(self):
        file = open('/home/giannis/Downloads/pair_end.txt')
        data =list(file)
        file.close()
        d= int(data[1])
        lines = [d.strip() for d in data[2:-2]]
        out = data[-1].strip()
        
        string = pairedReads(lines, d)
        assert string == out
        
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()