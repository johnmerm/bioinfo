'''    
Created on Dec 1, 2013

@author: giannis
'''
from MotifEnumeration import *
from MedianString import *
from random import random;
from random import randint
from bisect import bisect_left

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
            print ("found motifs "+ (" ".join(motifs))+" with score "+str(c_score))
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
 
def formProfile(kmer_list,laplace=True):
    profile=[]
    for i in range(len(kmer_list[0])):
        profile.append([0,0,0,0])
        for t in range(len(kmer_list)):
            ks = kmer_list[t][i];
            profile[i][index(ks)]+= 1
        if (laplace):
            mp = min(profile[i])
            if (mp==0):
                profile[i] = [p+1 for p in profile[i]]
            sp = sum(profile[i]) 
        profile[i] = [float(p)/float(sp) for p in profile[i]]
    return profile

def gibbsRandom(dna,k,profile):
    daKmers = []
    probs = []
    probInteg = []
    s = 0.0
    
    for i in range(len(dna)-k+1):
        daKmer = dna[i:i+k]
        daKmers.append(daKmer)
        prob = probability(daKmer, profile)
        probs.append(prob)
        probInteg.append(s)
        s += prob
    lo = 0
    hi = len(probInteg)
    
    r = random()*s
    i = bisect_left(probInteg, r,lo,hi)
    if i == hi:
        return daKmers[hi-1]
    else:
        return daKmers[i]
    

def plainRandom(dna,k):
    
    kmers=  list(kmersInDna(dna, k));
    return kmers[randint(0,len(kmers)-1)]
    
def randomSearch(dna_list,k,t):
    bestMotifs = []
    for i in range(t):
        bestMotifs.append(plainRandom(dna_list[i],k))
    
    best_score = score(bestMotifs, k)
    motifs = list(bestMotifs)
    while True:
        profile = formProfile(motifs)
        motifs = [profileMostProbableKMer(dna, k, profile) for dna in dna_list]
        sc = score(motifs,k)
        if sc<best_score:
            bestMotifs = motifs
            best_score = sc
        else:
            return (bestMotifs,best_score)


def gibbsSearch(dna_list,k,t,N):
    bestMotifs = []
    for i in range(0,t):
        bestMotifs.append(plainRandom(dna_list[i],k))
    best_score = score(bestMotifs, k)
    motifs = list(bestMotifs)
   
    for count in range(N):
        i = randint(0,len(motifs)-1)
        profileMatrix = [motifs[a] for a in range(t-1) if a !=i ]
        profile = formProfile(profileMatrix)
        motifs[i] = gibbsRandom(dna_list[i],k,profile)
        sc = score(motifs, k)
        if sc <best_score:
            best_score = sc
            bestMotifs = motifs
    return bestMotifs,best_score        
        
    
            
        
def gibbsSearchFull(dna_list,k,t,N):
    best_score=65535
    bestMotif = []
    for i in range(20):
        (r,s) = gibbsSearch(dna_list, k, t, N)
        if s<best_score:
            best_score = s
            bestMotif = r
    return bestMotif,best_score 

def randomSearchFull(dna_list,k,t):
    bs = 65535
    best = []
    for count in range(1000):
        (m,s) = randomSearch(dna_list, k, t)
        if s<bs:
            bs = s
            best = m
    return best
