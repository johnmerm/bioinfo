'''
Created on Jun 12, 2015

@author: grmsjac6
'''
import unittest

import spectrumGraph 
from time import time
from numpy import Inf


# masses = {'X':4,'Z':5}
# 

def scoreGraph(spectrum,_proteom = None,masses_rev = spectrumGraph.masses_rev,masses = spectrumGraph.masses):
    proteom = None
    if _proteom !=None:
        proteom = _proteom.replace('Q','K')
        proteom = proteom.replace('L','I')
    
    sgb = {i: {j:masses_rev[j-i][0] for j in range(i+1,len(spectrum)) if abs(j-i) in masses_rev} for i in range(len(spectrum)) }
    
    max_score = [-1]    
    ret_path = ['']
    start = time()
    def follow(path):
        
        if path[-1] in sgb and len(sgb[path[-1]])>0:
            nx = sgb[path[-1]]
            for n in nx:
                path_new = path+[n]
                pp = ''.join([sgb[path_new[i]][path_new[i+1]] for i in range(len(path)) ])
                
                if not proteom or  pp in proteom:
                    follow(path_new)
        else:
            if path[-1] == len(spectrum)-1:
                pp = ''.join([sgb[path[i]][path[i+1]] for i in range(len(path)-1) ])
                
                if not proteom or  pp in proteom:
                    score = sum(map(lambda p:spectrum[p],path))
                    
                    if score > max_score[0]:
                        max_score[0] = score
                        ret_path[0] = pp
                        #print score,ret_path,time()-start
                
                            
    
    follow([0])
    
    if proteom:
        idx = proteom.index(ret_path[0])
        ret_path[0] = _proteom[idx:idx+len(ret_path[0])]
        return ret_path[0],max_score[0]
    else:
        return ret_path[0],max_score[0]

def exam_scoreGraph():
    line = list(open('dataset_11813_10.txt'))[0].strip()
    spectrum = [int(v) for v in line.split()]
    
    path = scoreGraph(spectrum)
    print path    


def exam_scoreGraph2():
    lines = list(open('dataset_11866_2.txt'))
    spectrum = [int(v) for v in lines[0].strip().split()]
    proteom = lines[1].strip()
    path = scoreGraph(spectrum,proteom)
    print path

def exam_psm():
    
    
#     paths = ['QQCGVHEYFWVSKK',
#             'HTNGPDCSQYQLLK',
#             'VIAAGAHPADGQGVRGP',
#             'NGMPFCCMCWDVVM',
#             'AAPVCLQQMQPKAVL',
#             'SIAQIMVEYTVHGH',
#             'GRNPMLCTAIDKNK',
#             'KMARKRHIHKFLSP',
#             'NRAEQFDMTKYCV',
#             'ADMCRPCQACTGKAFG',
#             'CKFADFDSKTMGVITQ',
#             'RGVQTVWKASTPDII',
#             'DETTVPHLVCPWHD',
#             'IFWVHEMMYHCE',
#             'GWKRGTYEIIFCPP',
#             'DGQGVRGPHQIILMVR',
#             'TCFAAGAHVMRKGCH',
#             'DCQNYMLMHMVETG',
#             'CYCMFHTNTARGERK']
#     
#     
#     
    lines = list(open('dataset_11866_5.txt'))
    spectra_lines = lines[:-2]
    spectra = [[int(v) for v in line.strip().split()] for line in spectra_lines]
    proteom = lines[-2].strip()
    threshold = float(lines[-1])
#     
#     
#     scores = {path: max( {i:_score(path,spectra[i]) for i in range(len(spectra))  }.items(),key = lambda k:k[1]) for path in paths }
#     print scores
#     
#     
#     scoreGraph(spectra[1], proteom)
    
    
    psm_set,paths = psm(spectra,proteom,threshold)
    print '----------------------\n'
    
    print'\n'.join(psm_set)
    
def psm(spectra,proteom,threshold,masses_rev = spectrumGraph.masses_rev):
    psm_set = []
    paths = []
    for spectrum in spectra:
        path,score = scoreGraph(spectrum, proteom, masses_rev)
        paths.append((path,score))
        print path,score,score>=threshold
        if score>=threshold:
            
            psm_set.append(path)
    return psm_set,paths


def _score(path,spectrum,masses_rev = spectrumGraph.masses_rev,masses = spectrumGraph.masses):
    vector = [1]+spectrumGraph.spectrumVector(path,masses)
    
    lv = len(vector)
    ls = len(spectrum)
    if (ls !=lv):
        return -Inf
    else:
        values = [spectrum[i] for i in range(len(spectrum)) if vector[i]==1]
        return sum(values)

class Test(unittest.TestCase):
    def setUp(self):
        self.masses_rev = {4:['X'],5:['Z']}
        self.masses = {'X':4,'Z':5}
    
    def testScore(self):
        
        
        line = '0 0 0 0 4 -2 -3 -1 -7 6 5 3 2 1 9 3 -8 0 3 1 2 1 8'
        spectrum = [int(v) for v in line.split()]
        path,score = scoreGraph(spectrum,masses_rev=self.masses_rev,masses=self.masses)
        correctPath = 'XZZXX'
        assert path==correctPath
    
    def testScore2(self):
        lines = ['0 0 0 0 4 -2 -3 -1 -7 6 5 3 2 1 9 3 -8 0 3 1 2 1 8','XZZXZXXXZXZZXZXXZ'] 
                # 0 0 0 0 0  1  0  0  0 1 0 0 0 0 1 0  0 0 1 0 0 0 1
        spectrum = [int(v) for v in lines[0].strip().split()]
        proteom = lines[1].strip()
        path,score = scoreGraph(spectrum, proteom, self.masses_rev,self.masses)
        correctPath = 'ZXZXX'
        assert path==correctPath
    
    def testPSM(self):
        lines = ['0 -1 5 -4 5 3 -1 -4 5 -1 0 0 4 -1 0 1 4 4 4','1 -4 2 -2 -4 4 -5 -1 4 -1 2 5 -3 -1 3 2 -3','XXXZXZXXZXZXXXZXXZX','5' ]
                # 0  0 0  0 1 0  0  0 0  1 0 0 0  1 0 0 0 0 1
        spectra_lines = lines[:-2]
        spectra = [[int(v) for v in line.strip().split()] for line in spectra_lines]
        proteom = lines[-2].strip()
        threshold = float(lines[-1])
        
        psm_set = psm(spectra,proteom,threshold,self.masses_rev,self.masses)
        correctPSM = {'XZXZ'}
        assert psm_set == correctPSM

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    exam_psm()