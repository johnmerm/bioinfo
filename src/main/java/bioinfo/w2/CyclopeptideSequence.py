'''
Created on Nov 23, 2013

@author: giannis
'''
from Spectra import *
from timeit import itertools

def convolute(input,M):
    s_input=sorted([int(a) for a in input.split(" ")])
    s_input = [0]+s_input
    
    cv = [ [s_input[0]] ]
    
    freq = {}
    
    for i in range(1,len(s_input)):
        ccv =[s_input[i]]
        for j in range(1,i):
            ccvv = s_input[i] - s_input[j]
            ccv.append(ccvv)
            if ccvv >=57 and ccvv<=200:
                if ccvv in freq:
                    freq[ccvv]+=1
                else:
                    freq[ccvv] = 1
        cv.append(ccv)
        
    freq_s = sorted(freq.items(),key=lambda x:x[1],reverse=True)
    
    ret_freq = freq_s[:M]
    last_val = ret_freq[-1][1]
    for rf in freq_s[M:]:
        if rf[1] == last_val:
            ret_freq.append(rf)
        else:
            break
    
    ret_set = {s[0] for s in ret_freq}
        
    
     
    return ret_set,cv,freq_s

    
    

def filterAndRank(input,m):
    cv = [a for a in convolute(input) if a>=57 and a<=200]
    cvm = {}
    for a in cv:
        if a in cvm:
            cvm[a]+=1
        else:
            cvm[a]=1
    
    sorted_cvm = sorted(cvm.iteritems(),key=lambda x:x[1],reverse=True)
    cvm_final = []
    mc=0
    while mc<m:
        cvm_final.append(sorted_cvm[mc][0])
        mc +=1
    
    while sorted_cvm[mc][1] == sorted_cvm[m-1][1]:
        cvm_final.append(sorted_cvm[mc][0])
        mc+=1
    return [a[0] for a in sorted_cvm]

def expand(peptide,pep_set=i_set):#peptide being a sorted list of integers
    ret=list()
    ret.extend([peptide+[a] for a in pep_set])
    return ret

def score(spect,tgt):
    sc = 0;
    for s in spect:
        if s in tgt:
            sc+=1
    return sc

def spec_str(peptide):
    return "-".join([str(p) for p in peptide])
def CycloSequence(in_set,N=1,pep_set=i_set): #can't get it to work
    
    candidates = [[0]]
    prev_candidates = None
    
    candi_scores = {'':0}
    
    while len(candidates)>0:
        prev_candidates = candidates
        for c in list(candidates):
            parent_score = score(set(spectrum(c)), in_set)
            for cn in expand(c,pep_set):
                scor = score(spectrum(cn), in_set)
                if scor >parent_score:
                    candidates.append(cn)
                    candi_scores[spec_str(cn)] = scor
            
            #candidates.remove(c)
            
            
            candidates = sorted(candidates,key=lambda x:candi_scores[spec_str(x)] if spec_str(x) in candi_scores else 0,reverse=True)
            if len(candidates)>N :
                tie_can = candidates[:N]
                for ct in candidates[N:]:
                    if spec_str(ct) in  candi_scores and candi_scores[spec_str(ct)] == candi_scores[spec_str(candidates[N-1])]:
                        tie_can.append(ct)
                    else:
                        break
                
                candidates = tie_can
        if (candidates == prev_candidates):
            break
            
            
#             if (spect == in_set):
#                 candi_set.append(c)
#                 candidates.remove(c)
#             elif not spect.issubset(in_set):
#                 candidates.remove(c)
    
    
    candi_set = sorted(candidates,key=lambda x:candi_scores[spec_str(x)],reverse=True)
    
                
        
    
    return [spec_str(p[1:]) for p in candi_set]

def subpeptides(peptide):
    l = len(peptide)
    looped = peptide + peptide
    for start in range(0, l):
        for length in range(1, l):
            yield looped[start:start+length]

def spectrum(peptide):#peptide being a list of integers
#     if peptide == "":
#         return [0]
#     subs = subpeptides(peptide)
#     spct = [0]+ [sum([im_table[a] for a in ppd]) for ppd in subs]+[sum([im_table[a] for a in peptide])]
#     return sorted(spct);
    spec=set()
    for i in range(0,len(peptide)):
        combis = itertools.combinations(peptide,i)
        spec = spec.union({sum(c) for c in combis})
    return sorted(spec)
