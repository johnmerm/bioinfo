'''
Created on Dec 9, 2013

@author: grmsjac6
'''
import unittest
from bioinfo.w4.Contig import contigs


class Test(unittest.TestCase):


    def testContig(self):
        list=["ATG",
              "ATG",
              "TGT",
              "TGG",
              "CAT",
              "GGA",
              "GAT",
              "AGA"]
        cont = sorted(contigs(list))
        
        out="AGA ATG ATG CAT GAT TGGA TGT"
        assert " ".join(cont) == out

    

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testContig']
    unittest.main()