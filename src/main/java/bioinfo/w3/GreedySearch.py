'''    
Created on Dec 1, 2013

@author: giannis
'''
from MotifEnumeration import *
from MedianString import *

def index(k):
    if (k=='A'):return 0
    if (k=='C'):return 1
    if (k=='G'):return 2
    if (k=='T'):return 3

def probability(kmer,profile):
    prob = 1;
    for i in range(len(kmer)):
        ks = kmer[i]
        p = profile[i][index(ks)]
        prob *= p
    return prob

def profileMostProbableKMer(dna,k,profile):
    kmers = kmersInDna(dna, k);
    high_prob = 0;
    sel_kmer=None
    for kmer in kmers:
        if (sel_kmer == None): sel_kmer = kmer
        p = probability(kmer, profile)
        if p>high_prob:
            high_prob = p
            sel_kmer = kmer;
    return sel_kmer


  
def GreedyMotifSearch(dna_list,k,t):
    bestMotifs = [dna[0:k] for dna in dna_list]
    best_score = score(bestMotifs, k)
    
    for motif in kmersInDna(dna_list[0], k):
        motifs = [motif]
        for i in range(1,t):
            profile = formProfile(motifs[0:i])
            motifs.append(profileMostProbableKMer(dna_list[i], k, profile))
        c_score = score(motifs,k)
        if c_score<best_score:
            print "found motifs "+ (" ".join(motifs))+" with score "+str(c_score)
            bestMotifs = motifs
            best_score = c_score
    return bestMotifs

def score(motifs,k):
    col_score=[]
    for i in range(k):
        column = [motif[i] for motif in motifs]
        col_count = sorted({c:column.count(c) for c in set(column)}.items(),key=lambda x:x[1],reverse=True);
        col_score.append(len(column)-col_count[0][1])
    return sum(col_score)
 
def formProfile(kmer_list):
    profile=[]
    for i in range(len(kmer_list[0])):
        profile.append([0,0,0,0])
        for t in range(len(kmer_list)):
            ks = kmer_list[t][i];
            profile[i][index(ks)]+= 1
        #Laplace succession
        mp = min(profile[i])
        if (mp==0):
            profile[i] = [p+1 for p in profile[i]]
        
        sp = sum(profile[i]) 
        profile[i] = [float(p)/float(sp) for p in profile[i]]
    return profile

data = [ d.strip() for d in list(open('/home/giannis/Downloads/dataset_39_5(3).txt'))[1:] ]
gms = GreedyMotifSearch(data,12,25)

print "\n".join(gms)

