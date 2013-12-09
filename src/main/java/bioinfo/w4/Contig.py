'''
Created on Dec 9, 2013

@author: grmsjac6
'''
from StringComposition import deBru, revgraph

def contigList(graph,rev_graph):
    ctgs = []
    all_keys = set(graph.keys()).union(set(rev_graph.keys()))
    
    branches = [a for a in all_keys if not (a in graph and a in rev_graph and len(graph[a])==1 and len(rev_graph[a])==1)]
    
    for b in branches:
        if not b in graph:
            continue
        
        for c in graph[b]:
            contig = [b,c]
            while not c in branches:
                c = graph[c][0]
                contig.append(c)
            ctgs.append(contig)
    return ctgs

def contigs(tokens):
    ctg_strings = []
    graph = deBru(tokens)
    rev_graph = revgraph(graph)
    ctgs = contigList(graph, rev_graph)
    for ctg in ctgs:
        string = ctg[0]
        for ct in ctg[1:]:
            string += ct[-1]
        ctg_strings.append(string)
    
    return ctg_strings


def assignment():
    file = open('/home/giannis/Downloads/dataset_59_5.txt')
    data = list(file)
    file.close()
    lines = [d.strip() for d in data]
    ct = sorted(contigs(lines))
    print ("\n".join(ct))
