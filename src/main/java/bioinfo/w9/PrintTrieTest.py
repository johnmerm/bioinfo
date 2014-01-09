'''
Created on Jan 9, 2014

@author: grmsjac6
'''
import unittest
from Trie import printTrie,Trie

class Test(unittest.TestCase):
    

    def testPrintTrie(self):
        patterns = ["GGTA","CG","GGC"]
        trie = Trie(patterns)
        printTrie(trie, id)
        pass


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testPrintTrie']
    unittest.main()