'''
Created on Jan 8, 2014

@author: grmsjac6
'''
import unittest
from BreakDistance import breakDistance,breakDistanceFile

class Test(unittest.TestCase):


    def testBreakDistance(self):
        genomes=[[[+1,+2,+3,+4,+5,+6]],
                 [[1,-3,-6,-5],[2,-4]]]
        
        distance = breakDistance(genomes)
        assert distance ==3

    def testParse(self):
        genomeStrings = ["(+1 +2 +3 +4 +5 +6)\n",
                         "(+1 -3 -6 -5)(+2 -4)\n"]
        distance = breakDistanceFile(genomeStrings)
        assert distance ==3
    
    def testAssignment(self):
        f = open('dataset_89_1.txt')
        g = list(f)
        print(breakDistanceFile(g))
        pass
   
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testBreakDistance']
    unittest.main()