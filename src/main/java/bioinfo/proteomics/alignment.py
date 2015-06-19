'''
Created on Jun 19, 2015

@author: grmsjac6
'''
import unittest
import spectrumGraph
from numpy import Inf



    


def alignment(peptide,spectrum,k,masses = spectrumGraph.masses,masses_rev=spectrumGraph.masses_rev):
    

    
    def previous(i,j,t):
        yjf = j-masses[peptide[i-1]]-(masses[peptide[i-2]] if i>1 else 0)
       
        
        yjf = max(0,yjf)
        
        
        prevs = []
        for yj in range(yjf,j):
            tn = t if (yj == j-masses[peptide[i-1]]) else t-1
            if i>0 and tn>=0:
                prevs.append((i-1,yj,tn))
        return prevs
    
    def score((i,j,t),score_cache = {}):
        if (i,j,t) not in score_cache:
            if (i,j,t)==(0,0,0):
                score_cache[(i,j,t)] = (0,None)
            elif i==0 or j == 0:
                score_cache[(i,j,t)] = (-Inf,None)
            else:
                prvs = previous(i,j,t)
                if len(prvs) == 0:
                    sc = -Inf
                    score_cache[(i,j,t)] = (sc,None)
                else:
                    scores = [(score(p,score_cache),p) for p in prvs]
                    backtrack = max(scores)
                    sc = spectrum[j]+backtrack[0]
                    score_cache[(i,j,t)] = (sc,backtrack[1])
        return score_cache[(i,j,t)][0]
    
    end_pep = len(peptide)
    end_spec = len(spectrum)-1
    
    cache = {}
    
    
    
    scores_end = [(score((end_pep,end_spec,i),cache),i) for i in range(k+1)]
    sm = max(scores_end)
    
    path = []
    tt = (end_pep,end_spec,sm[1])
    while tt !=None:
        path = [tt]+path
        tt = cache[tt][1] if tt in cache else None
    
    
    spec = [0]
    for p in peptide:
        spec.append(spec[-1]+masses[p])
    
    pj = [path[i][1] for i in range(len(path))]
    
    
    pt = []
    for i in range(1,len(path)):
        c = peptide[i-1]
        df = pj[i]-pj[i-1]
        pt.append((c,df-masses[c]))
    return ''.join([p[0]+('('+'{0:+}'.format(p[1])+')' if p[1]!=0 else '') for p in pt]),sm[0],pt

def exam_alignment(fl,alPep):
    lines = list(open(fl))
    peptide = lines[0].strip()
    spectrum = [0]+[int(s) for s in lines[1].strip().split()]
    k = int(lines[2].strip())
    
    a,score,ap = alignment(peptide, spectrum, k)
    print a
    if alPep:
        sc_t = calcScore(alPep, spectrum)
        sc_m = calcScore(ap, spectrum)
        print score,sc_m,sc_t
    
    return a

def calcScore(alignedPep,spectrum,masses = spectrumGraph.masses):
    spec = [0]
    for (p,d) in alignedPep:
        spec.append(spec[-1]+masses[p]+d)
    
    score = sum([spectrum[i] for i in spec])
    return score
class Test(unittest.TestCase):
    def setUp(self):
        self.masses_rev = {4:['X'],5:['Z']}
        self.masses = {'X':4,'Z':5}

    def testAlignment(self):
        lines = ['XXZ','4 -3 -2 3 3 -4 5 -3 -1 -1 3 4 1 -1','2']
        peptide = lines[0].strip()
        spectrum = [0]+[int(s) for s in lines[1].strip().split()]
        k = int(lines[2].strip())
        
        out = 'XX(-1)Z(+2)'
        a,score,alPep = alignment(peptide, spectrum, k, self.masses, self.masses_rev)
        assert a == out
    def testExamAlignment(self):
        alPep = [('L',-61),('V',0),('W',-9),('S',0),('T',0),('E',69)]
        a = exam_alignment('dataset_alignment.txt',alPep)
        assert a == 'L(-61)VW(-9)STE(+69)'
        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    exam_alignment('dataset_11866_14.txt', None)