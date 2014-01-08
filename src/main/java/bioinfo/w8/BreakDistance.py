'''
Created on Jan 7, 2014

@author: grmsjac6
'''

import re

def appendToGraph(graph,n,c):
    if n in graph:
        graph[n].append(c)
    else:
        graph[n] = [c]
    #add the reverse also
    if c in graph:
        graph[c].append(n)
    else:
        graph[c] = [n]

def breakDistance(genomes):
    graph = {}
    blocks = set()
    
    for genome in genomes:
        for part in genome:
            for i in range(len(part)):
                p_this = part[i]
                p_prev = part[i-1]
                appendToGraph(graph, p_prev, -p_this)
                #appendToGraph(graph, -p_this, p_this)
                blocks.add(p_this if p_this>0 else -p_this)
    
    cycles = []
    
    while len(graph.keys())>0:
        start  = list(graph.keys())[0]
        cycle = []
        n = start
        while True:
            connections = graph[n]
            cycle.append(n)
            
            c = connections[0]
            del connections[0]
            if len(connections) == 0:
                del graph[n]
            
            graph[c].remove(n)
            if len(graph[c]) == 0:
                del graph[c]
            n = c
            if n == start:
                cycle.append(start)
                break
        cycles.append(cycle)
    return len(blocks) - len(cycles)

    
def breakDistanceFile(genomeStrings):
    genomes = []
    
    for genomeString in genomeStrings:
        genomeParts = re.findall("\(([^\)|\(]*)\)", genomeString)
        genome = []
        for genomePart in genomeParts:
            genome.append([int(p) for p in genomePart.split(" ")])
        genomes.append(genome)
    return breakDistance(genomes)
        
       
    
    
def complement(s):
    if s == 'A':return 'T'
    elif s=='T':return 'A'
    elif s=='C':return 'G'
    elif s=='G':return 'C'
def reverse_complement(kmer):
    rev = "".join([complement(s) for s in reversed(kmer)])
    return rev
    
def all_kmers(v,k):
    kmers = []
    kmer_idx = {}
    for i in range(len(v)-k+1):
        kmer = v[i:i+k]
        kmers.append(kmer)
        if kmer in kmer_idx:
            kmer_idx[kmer].append(i)
        else:
            kmer_idx[kmer] = [i]
            
    return kmers,kmer_idx

def sharedKmers(k,v,w):
    vk,vk_idx = all_kmers(v, k)
    wk,wk_idx = all_kmers(w, k)
    pos=[]
    
    for kmer,i_pos in vk_idx.items():
        j_pos = wk_idx[kmer] if kmer in wk_idx else []
        jr_pos = wk_idx[reverse_complement(kmer)] if reverse_complement(kmer) in wk_idx else []
        
        for i in i_pos:
            for j in j_pos:
                pos.append((i,j))
            for j in jr_pos:
                pos.append((i,j))
    
    return pos

    
def assignment(): 
    f = open('dataset_90_2.txt')
    k=int(next(f))
    v=next(f).strip()
    w=next(f).strip()
    
    t= sharedKmers(k, v, w)
    print("\n".join([ "("+str(ti[0])+", "+str(ti[1])+")" for ti in t]))

        
            