'''
Created on Dec 1, 2013

@author: giannis
'''
import unittest
from MotifEnumeration import *

class Test(unittest.TestCase):


    def testMotifEnumeration(self):
        k=3
        d=1
        dna_list = ["ATTTGGC","TGCCTTA","CGGTATC","GAAAATT"]
        output = {"ATA","ATT","GTT","TTT"}
        input = set(motifEnumeration(dna_list,k,d))
        assert output == input

    
    def testMotifEnumerationWithDataSet(self):
        datafile = list(open('motif_enumeration_data.txt'))
        k = int(datafile[1].split(" ")[0])
        d = int(datafile[1].split(" ")[1])
        dna_list = [dd.strip() for dd in datafile[2:8]]
        output = {dd.strip() for dd in datafile[9].split(" ")}
        input = set(motifEnumeration(dna_list,k,d))
        assert output == input
        
    def testMotifEnumerationWithActualData(self):
        
        k = 5
        d = 1
        dna_list = ["GAATAAGGCCCTGTCATCTCTTATT",
                    "GTCTACTGGTGATTAAGATACGCCC",
                    "GATTACGCACGGGGAGCGAGCAAGA",
                    "GGGTTGATTAAGCCCGACTAGTCGG",
                    "AATTAGATTACTGGCTCGTGAGTCG",
                    "AACGCCCCAAGAATACAAAGGATGC"]
        input = set(motifEnumeration(dna_list,k,d))
        print " ".join(input)
        
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testMotifEnumerationWithDataSet']
    unittest.main()