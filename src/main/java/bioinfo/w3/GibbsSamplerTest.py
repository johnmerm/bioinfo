'''
Created on Dec 2, 2013

@author: grmsjac6
'''
import unittest
from bioinfo.w3.GreedySearch import gibbsSearchFull, score


class Test(unittest.TestCase):


    def testGibbsSearch(self):
        k=8
        t=5
        N=100
        data =["CGCCCCTCTCGGGGGTGTTCAGTAAACGGCCA",
               "GGGCGAGGTATGTGTAAGTGCCAAGGTGCCAG",
               "TAGTACCGAGACCGAAAGAAGTATACAGGCGT",
               "TAGATCAAGTTTCAGGTGCACGTCGGTGAACC",
               "AATCCACCAGCTCCACGTGCAATGTTGGCCTA"]

        out= ["TCTCGGGG",
              "CCAAGGTG",
              "TACAGGCG",
              "TTCAGGTG",
              "TCCACGTG"]
        
        res = gibbsSearchFull(data, k, t, N)
        
        so = score(out, k)
        sr = score(res,k)
        assert  sr <= so

    def gibbsSearchOut(self):
        k=15
        N=2000   
        data = [ d.strip() for d in list(open('C:/Users/grmsjac6.GLOBAL-AD/Downloads/dataset_43_4.txt'))[1:] ]

        t=len(data)
        r,s = gibbsSearchFull(data, k, t, N)
        
        print("\n".join(r))
        print(score(r, k))


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testGibbsSearch']
    unittest.main()