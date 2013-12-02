'''
Created on Dec 1, 2013

@author: giannis
'''


dna_string=['A','C','G','T'];

def kmersInDna(dna,k):
    kid = set()
    for i in range(len(dna)-k+1):
        kid.add(dna[i:i+k]);
    return kid

def freqKmersInDna(dna,k):
    kid = list()
    for i in range(len(dna)-k+1):
        kid.append(dna[i:i+k]);
    return {t:kid.count(t) for t in set(kid)}

def mutateSingleKmer(kmer):
    muts = set()
    for i in range(len(kmer)):
        mut = list(kmer);
        for j in range(len(dna_string)):
            mut[i] = dna_string[j]
            muts.add("".join(mut))
    return muts
    
    
def mutateKmer(kmer,d):
    muts = {kmer};
    for i in range(d):
        for k in muts:
            muts = muts.union(mutateSingleKmer(k))
    return muts


def mutateKmers(kmers,d):
    muts=set()
    for kmer in kmers:
        muts = muts.union(mutateKmer(kmer,d))
    return muts

def motifEnumeration(dna_list,k,d):
    kmers=set()
    for dna in dna_list:
        kmers = kmers.union(kmersInDna(dna,k))
    
    kmuts = mutateKmers(kmers, d)
    candidates = {km:mutateKmer(km,d) for km in kmuts}
    
    for (c,v) in candidates.items():
        found = True
        for dna in dna_list:
            dnaKmers = kmersInDna(dna,k)
            cv = {vv for vv in v if vv in dnaKmers}
            found = found and len(cv)>0 
        if found:
            yield c
    
    


