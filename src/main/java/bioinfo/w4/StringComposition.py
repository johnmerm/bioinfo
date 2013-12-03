'''
Created on Dec 3, 2013

@author: grmsjac6
'''
from bioinfo.w3.MotifEnumeration import kmersInDna,allKmersInDna
from random import randint

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
    

def parseGraph(lines):
    graph = {}
    for line in lines:
        toks = line.split(" -> ")
        graph[toks[0]]=toks[1].strip().split(",")
    return graph

def copyGraph(graph):
    return {k:list(v) for k,v in graph.items() }

def eulerCycles(graph,cycle=[],n=None,cycles=[]):
    cg = copyGraph(graph)
    if n == None:
        n = list(cg.keys())[randint(0,len(cg)-1)]
    startN = cycle[0] if len(cycle)>0 else n
    while True:
        cycle.append(n)
        connections = [c for c in cg[n] if (not c in cycle or c == startN)]
        del cg[n]
        if len(connections) == 0:
            break
        elif len(connections) >1:
            for ni in connections:
                thisCycle = list(cycle)
                cycles.append(thisCycle)
                eulerCycles(cg, thisCycle, ni, cycles)
        else:
            n = connections[0]
        
        
        if len(cycle) == len(cg) and n == cycle[0]:
            break
    return cycles
    
     


lines =["0 -> 3",
        "1 -> 0",
        "2 -> 1,6",
        "3 -> 2",
        "4 -> 2",
        "5 -> 4",
        "6 -> 5,8",
        "7 -> 9",
        "8 -> 7",
        "9 -> 6"]

graph=parseGraph(lines)

cycles = eulerCycles(graph)

fullCycles = [cycle for cycle in cycles if len(cycle)== len(graph) and cycle[0] == cycle[len(cycle)-1] ]

print(fullCycles)
        