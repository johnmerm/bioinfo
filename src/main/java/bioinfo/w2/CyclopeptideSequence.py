'''
Created on Nov 23, 2013

@author: giannis
'''
from timeit import itertools
from bioinfo.w2.Spectra import i_set

def convolute(input):
    s_input=sorted([int(a) for a in input.split(" ")])
    for i in range(0,len(s_input)):
        ai = s_input[i]
        for j in range(0,i):
            aj = s_input[j]
            a = ai-aj
            yield a
    

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

def expand(peptideList):
    ret=list()
    for peptide in peptideList:
        ret.extend([peptide+a for a in i_set])
    return ret

def score(spect,tgt):
    sc = 0;
    for s in spect:
        if s in tgt:
            sc+=1
    return sc

def CycloSequence(in_set,N=1): #can't get it to work
    
    candidates = [""]
    prev_candidates = None
    
    candi_scores = {'':0}
    
    while len(candidates)>0:
        prev_candidates = candidates
        for c in list(candidates):
            parent_score = score(set(spectrum(c)), in_set)
            for cn in expand([c]):
                scor = score(set(spectrum(cn)), in_set)
                if scor >parent_score:
                    candidates.append(cn)
                    candi_scores[cn] = scor
            
            #candidates.remove(c)
            
            
            candidates = sorted(candidates,key=lambda x:candi_scores[x],reverse=True)
            if len(candidates)>N :
                tie_can = candidates[:N]
                for ct in candidates[N:]:
                    if candi_scores[ct] == candi_scores[candidates[N-1]]:
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
    
    
    candi_set = sorted(candidates,key=lambda x:candi_scores[x],reverse=True)
    
                
        
    ret_set = set()
    for c in candi_set:
        r = "-".join([str(im_table[ci]) for ci in c])
        ret_set.add(r)
    
    
    return ret_set

def subpeptides(peptide):
    l = len(peptide)
    looped = peptide + peptide
    for start in range(0, l):
        for length in range(1, l):
            yield looped[start:start+length]


im_table_file = open('integer_mass_table.txt')
im_table = {s.split(' ')[0]:int(s.split(' ')[1])  for s in im_table_file }
integer_dict = {im_table[x]:x for x in im_table}
i_set = set(integer_dict.values())

def spectrum(peptide):
    if peptide == "":
        return [0]
    subs = subpeptides(peptide)
    spct = [0]+ [sum([im_table[a] for a in ppd]) for ppd in subs]+[sum([im_table[a] for a in peptide])]
    return sorted(spct);
