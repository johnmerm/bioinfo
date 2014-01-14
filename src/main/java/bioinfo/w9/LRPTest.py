'''
Created on Jan 14, 2014

@author: grmsjac6
'''
import unittest
from Trie import longestRepeat

class Test(unittest.TestCase):


    def testLRP(self):
        text = 'ATATCGTTTTATCGTT'
        lrp = longestRepeat(text)
        assert lrp=='TATCGTT'
        


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testLRP']
    unittest.main()