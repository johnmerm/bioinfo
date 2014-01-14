'''
Created on Jan 14, 2014

@author: grmsjac6
'''
import unittest
from Trie import SuffixTrie,longestRepeat,compressSuffixTrie

class Test(unittest.TestCase):

    def testCompress(self):
        text='panamabananas'
        root = SuffixTrie(text)
        root,all_nodes = compressSuffixTrie(root)
        pass
    def testLRP(self):
        #text = 'ATATCGTTTTATCGTT'
        text='panamabananas'
        lrp = longestRepeat(text)
        assert lrp=='TATCGTT'
        


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testLRP']
    unittest.main()