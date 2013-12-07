'''
Created on Dec 7, 2013

@author: giannis
'''
from bioinfo.w4.EulerGraph import paths, cycle
from StringComposition import deBru
def StringReconstruction(graph,rev_graph):
    p = paths(graph, rev_graph)
    string = p[0]
    for ps in p[1:]:
        sf = ps[-1]
        string+=sf
    return string

def createKmers(k):
    kmers=['']
    for i in range(k):
        kmers2 = ['0'+j for j in kmers]+['1'+j for j in kmers]
        kmers = kmers2
    return kmers

def UniversalString(k):
    kmers= createKmers(k)
    graph = deBru(kmers)
    rev_graph = {}
    for (n,cc) in graph.iteritems():
        for c in cc:
            if c in rev_graph:
                rev_graph[c].append(n)
            else:
                rev_graph[c]=[n]
    p = cycle(graph, rev_graph, kmers[0][1:])
    r=""
    s=""
    for pi in p[:-1]:
        r+=pi[-1]
        #print s+pi
        #s=s+" "
    print(r)
    return r

def find_all(string,kmer):
    occ=[]
    pos =-1
    while True:
        pos = string.find(kmer,pos+1)
        if pos !=-1:
            occ.append(pos)
        else:
            break
    return occ 
        
def validateUniversalString(string,k):
    kmers = createKmers(k)
    if len(string) != pow(2, k):
        return False
    valString = string+string
    
    found = True
    for kmer in kmers:
        pos = find_all(valString, kmer)
        if len(pos) == 2:
            continue
        elif len(pos)==1:
            if pos[0]< len(string)-k or pos[0]>len(string):
                return False
        else:
            return False 
    return True

print validateUniversalString(UniversalString(16), 16)
