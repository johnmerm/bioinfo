'''
Created on Dec 10, 2013

@author: grmsjac6
'''
import unittest
from CyclopeptideSequence import convolute
from bioinfo.w2.CyclopeptideSequence import CycloSequence

class Test(unittest.TestCase):


    def testConvolute(self):
        M=20
        N=60
        input = "57 57 71 99 129 137 170 186 194 208 228 265 285 299 307 323 356 364 394 422 493"
        in_set = {int(s) for s in input.split(" ")}
        in_set.add(0)
        
        pep_set,cv,freq_s = convolute(input,M)
        for c in cv:
            print (" ".join([str(i) for i in c]))
        
        for (c,v) in freq_s:
            print (str(c)+":"+str(v))
            
        print(" ".join([str(s) for s in pep_set]))
        
        
        ret_set = CycloSequence(in_set,  N, pep_set)
        
        testable = {frozenset({int(i) for i in s.split("-")}) for s in ret_set}
        
        comp_set = frozenset({int(i) for i in "99-71-137-57-72-57".split("-")})
        print(ret_set)
        
        assert comp_set in testable
        pass


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()