'''
Created on Dec 3, 2013

@author: grmsjac6
'''
from bioinfo.w3.MotifEnumeration import kmersInDna,allKmersInDna
from random import randint
from timeit import itertools

def composition(dna,k):
    kmers = allKmersInDna(dna, k)
    return sorted(kmers)

def overlap(dna_list):
    overlaps = []
    k = len(dna_list[0])
    prefix={}
    suffix={}
    dna_copy = list(dna_list)
    for dna in dna_list:
        p = dna[:k-1]
        s = dna[1:k]
        if p in prefix:
            prefix[p].append(dna)
        else:
            prefix[p]=[dna]
        
        if s in suffix:
            suffix[s].append(dna)
        else:
            suffix[s] = [dna]
    
    for s in suffix.keys():
        if s in prefix:
            overlaps+= [(sv,pv) for sv in suffix[s] for pv in prefix[s] ]
    
    return sorted(overlaps,key=lambda x:x[0])

def deBruin(dna,k):
    kmers = allKmersInDna(dna, k-1)
    overlaps = overlap(kmers)
    debru = {}
    for (s,p) in overlaps:
        if s in debru:
            debru[s].add(p)
        else:
            debru[s] = {p}
    return sorted(debru.items(),key=lambda x:x[0])


def deBru(kmers):
    debru = {}
    overlaps = []
    for kmer in kmers:
        k = len(kmer)
        overlaps.append( (kmer[:k-1],kmer[1:]) )
    for (s,p) in overlaps:
        if s in debru:
            debru[s].add(p)
        else:
            debru[s] = {p}
    
    return sorted(debru.items(),key=lambda x:x[0])
