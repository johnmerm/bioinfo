'''
Created on Jan 14, 2014

@author: giannis
'''
import unittest
from SuffixArray import SuffixArray

class Test(unittest.TestCase):


    def a_testSuffixArray(self):
        text = 'AACGATAGCGGTAGA$'
        sar = SuffixArray(text)
        print(sar)
        sart = [15, 14, 0, 1, 12, 6, 4, 2, 8, 13, 3, 7, 9, 10, 11, 5]
        assert sar == sart

    def testAssignment(self):
        f=open('dataset_96_3.txt')
        text = next(f).strip()
        sar = SuffixArray(text)
        print(sar)
        pass

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testSuffixArray']
    unittest.main()