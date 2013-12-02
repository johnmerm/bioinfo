'''
Created on Nov 23, 2013

@author: giannis
'''
from timeit import itertools


im_table_file = open('integer_mass_table.txt')

im_table = {s.split(' ')[0]:int(s.split(' ')[1])  for s in im_table_file }



rev_table = dict()
for v in im_table.values():
    rev_table[v]= {a for a in im_table.keys() if im_table[a] == v}


def subpeptides(peptide):
    l = len(peptide)
    looped = peptide + peptide
    for start in range(0, l):
        for length in range(1, l):
            yield looped[start:start+length]



    
def spectrum(peptide):
    if peptide == "":
        return [0]
    subs = subpeptides(peptide)
    spct = [0]+ [sum([im_table[a] for a in ppd]) for ppd in subs]+[sum([im_table[a] for a in peptide])]
    return sorted(spct);

integer_dict = {im_table[x]:x for x in im_table}
i_set = set(integer_dict.values())

def expand(peptideList):
    ret=list()
    for peptide in peptideList:
        ret.extend([peptide+a for a in i_set])
    return ret

def CycloSequence(in_set): #can't get it to work
    ret_set =[]
    candidates = [""]
    while len(candidates)>0:
        
        candidates = expand(candidates)
        for c in candidates:
            
            spect = set(spectrum(c))
            if (spect == in_set):
                ret_set.append(spect)
                candidates.remove(c)
            elif not spect.issubset(in_set):
                candidates.remove(c)
     
        
        
    return ret_set    
                
    
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
     
        
in_str="0 113 128 186 241 299 314 427"
print(CycloSequence({int(a) for a in in_str.split(" ")}))            

