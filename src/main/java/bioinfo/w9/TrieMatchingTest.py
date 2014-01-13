'''
Created on Jan 9, 2014

@author: grmsjac6
'''
import unittest
from Trie import printTrie,Trie,trieMatching

class Test(unittest.TestCase):
    

    def a_testPrintTrie(self):
        patterns = ["GGTA","CG","GGC"]
        trie = Trie(patterns)
        printTrie(trie, id)
        pass
    
    def a_testTrieMatching(self):
        text='AATCGGGTTCAATCGGGGT'
        patterns=['ATCG','GGGT']
        m = trieMatching(text, patterns)
        ma = []
        for v in m.values():
            ma += v
        print(" ".join([str(mv) for mv in sorted(ma)]))
    
    def testAssignment(self):
        f = open('dataset_93_6.txt')
        toks = list(f)
        text = toks[0].strip()
        patterns = [t.strip() for t in toks[1:]]
        
        m = trieMatching(text, patterns)
        ma = []
        for v in m.values():
            ma += v
        print(" ".join([str(mv) for mv in sorted(ma)]))
        
    


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testPrintTrie']
    unittest.main()