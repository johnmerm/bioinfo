'''
Created on Dec 7, 2013

@author: giannis
'''
import unittest
from bioinfo.w4.Contigs import findContigs


class Test(unittest.TestCase):


    def testContigs(self):
        lines=  ["ATG",
                 "ATG",
                 "TGT",
                 "TGG",
                 "CAT",
                 "GGA",
                 "GAT",
                 "AGA"]
        contigs = findContigs(lines)
        out=["AGA","ATG","ATG","CAT","GAT","TGGA","TGT"]
        
        assert contigs == out


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testContigs']
    unittest.main()