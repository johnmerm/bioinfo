'''
Created on Dec 1, 2013

@author: giannis
'''

from MotifEnumeration import *
def allKmersOfLength(k):
    ret={''}
    for i in range(k):
        for r in ret:
            ret = ret.union({r+a for a in dna_string})
            ret.remove(r)
    return ret


def diffKmer(kmer1,kmer2):
    d=0;
    for i in range(len(kmer1)):
        if (kmer1[i]!=kmer2[i]):
            d += 1
    return d

def diffOneDna(dna,kmer):
    kmers = kmersInDna(dna, len(kmer))
    diffs = [diffKmer(kmer1,kmer) for kmer1 in kmers]
    return min(diffs)

def diff (dna_list,kmer):
    diffs = [diffOneDna(dna,kmer) for dna in dna_list]
    return sum(diffs)



def median_string(dna_list,k):
    bestPattern='';
    d= 65535;
    for pattern in allKmersOfLength(k):
        di = diff(dna_list,pattern) 
        if (di <d):
            bestPattern = pattern;
            d = di
    
    return bestPattern;
    
k=6
dna_list=["GTACACTGCGGTTAGCTGGAGTAAGGAGAGTGGTCGGCGCCA",
          "TGGTCCCTCGTTCACCTGACCATATAGGTCATAGTCATCTTA",
          "CCCATCCAACTCTGGTCTCTATAAAGTCTTAATAATCACTGC",
          "TGGTCAGCGGAAAACGGACCGGCGACCGCAACGGGCACAGAG",
          "TGGTCTGAATGGAATTAACAGTGCCGTAATGTCGGTGTCCAG",
          "GTTCGCTACTCGTACAGATCCTGCACCGCGTGGTCTTCCTCG",
          "TGGTCAACGAAAAACGAGTCTATGGCCGATTTTAATGTTTGA",
          "TTTAACTGCGTTGTTGATTGGTCGCTCCCAGATCTGATTGGA",
          "TGGTCCCAGAGGGAGTGTAAAATTGGCGGTACACGTTTGAAA",
          "ATAGGCCGTGGATTTGACAGAAACCCGGAATGGTCGAATATA"
          ]


 