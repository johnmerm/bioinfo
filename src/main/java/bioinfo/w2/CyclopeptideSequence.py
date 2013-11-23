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

def expand(peptide):
    return [peptide+a for a in im_table.keys()]

def CycloSequence(input): #can't get it to work
    in_set = {int(a) for a in input.split(" ")}
    ret_set =set()
    candidates = [""];
    while True:
        next_phase=[]
        for c in candidates:
            spc = set(spectrum(c))
            if (spc == input):
                ret_set.add("-".join([str(im_table[c1]) for c1 in c]))
            elif spc.issubset(in_set):
                next_phase.append(c)
            
            
        if len(next_phase) == 0:
            break;
        candidates=[]
        for n in next_phase:
            candidates.extend(expand(n))
             
    return ret_set    
                
    
def convolute(input):
    s_input=sorted([int(a) for a in input.split(" ")])
    for i in range(1,len(s_input)):
        ai = s_input[i]
        yield ai
        for j in range(1,i):
            aj = s_input[i-j]
            a = ai-aj
            yield a
    

print(list(convolute("465 473 998 257 0 385 664 707 147 929 87 450 748 938 998 768 234 722 851 113 700 957 265 284 250 137 317 801 128 820 321 612 956 434 534 621 651 129 421 337 216 699 347 101 464 601 87 563 738 635 386 972 620 851 948 200 156 571 551 522 828 984 514 378 363 484 855 869 835 234 1085 764 230 885"))  )
            
             
            

