'''
Created on Jun 15, 2015

@author: grmsjac6
'''
import unittest
import spectrumGraph
from numpy import NaN


def size(i,t,spectrum,masses=spectrumGraph.masses,size_cache={},factor = 1.):
    if not (i,t) in size_cache:
        if i==0:
            if t == 0:
                sz = 1
            else:
                sz = 0
        elif i<0:
            sz = 0
        else:
            sz = sum([factor*size(i-a,t-spectrum[i],spectrum,masses,size_cache,factor) for a in masses.values()])
        size_cache[(i,t)] = sz
    return size_cache[(i,t)]


def dictionarySize(spectrum,threshold,max_score,masses=spectrumGraph.masses):
    m = len(spectrum)-1
    
    cache = {}
    sz =  sum([size(m,t,spectrum,masses,size_cache=cache) for t in range(threshold,max_score)])
    return sz,cache

def dictionaryProbability(spectrum,threshold,max_score,masses=spectrumGraph.masses):
    m = len(spectrum)-1
    cache = {}
    prb = sum([size(m,t,spectrum,masses,cache,1./len(masses)) for t in range(threshold,max_score)])
    return prb
    
def exam_dictionarySize(fl='dataset_11866_8.txt',includeZero = False):
    lines = list(open(fl))
    spectrum = [int(s) for s in lines[0].strip().split()]
    if not includeZero:
        spectrum = [NaN]+spectrum
    threshold = int(lines[1].strip())
    max_score = int(lines[2].strip())
        
    dictSize,cache = dictionarySize(spectrum, threshold, max_score)
    
    
    
    print dictSize
    return dictSize
    
def exam_probability(fl='dataset_11866_11.txt',includeZero = False):
    lines = list(open(fl))
    spectrum =[int(s) for s in lines[0].strip().split()]
    
    if not includeZero:
        spectrum = [NaN]+spectrum
    
    threshold = int(lines[1].strip())
    max_score = int(lines[2].strip())
        
    prb = dictionaryProbability(spectrum, threshold, max_score)
    print prb
class Test(unittest.TestCase):
    def setUp(self):
        self.masses_rev = {4:['X'],5:['Z']}
        self.masses = {'X':4,'Z':5}

    def testDictionarySize(self):
        lines = ['0 4 -3 -2 3 3 -4 5 -3 -1 -1 3 4 1 -1','1','5']
        spectrum = [int(s) for s in lines[0].strip().split()]
        threshold = int(lines[1].strip())
        max_score = int(lines[2].strip())
        
        dictSize,cache = dictionarySize(spectrum, threshold, max_score, self.masses)
        print dictSize
        assert dictSize == 3
    
    def testExtraDictionary(self):
        sz = exam_dictionarySize('dataset_size.txt',True)
        assert sz == 330
    def testProbability(self):
        lines = ['0 4 -3 -2 3 3 -4 5 -3 -1 -1 3 4 1 -1','1','5']
        spectrum = [int(s) for s in lines[0].strip().split()]
        threshold = int(lines[1].strip())
        max_score = int(lines[2].strip())
         
        prb = dictionaryProbability(spectrum, threshold, max_score, self.masses)
        print prb
        assert prb == 0.375
    def testExtraProbability(self):
        pb = exam_probability('dataset_probability.txt',True)
        assert pb == 0.00132187890625
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    exam_probability()
    