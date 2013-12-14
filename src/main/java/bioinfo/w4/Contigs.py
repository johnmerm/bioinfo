'''
Created on Dec 7, 2013

@author: giannis
'''
from bioinfo.w4.StringComposition import deBru
from bioinfo.w4.EulerGraph import reverse_graph


def findContigs(kmers):
    contigs = []
    graph = deBru(kmers);
    rev_graph = reverse_graph(graph)
    
    all_nodes = list(set(graph.keys()).union(set(rev_graph.keys())))
    
    branches = [n for n in all_nodes if (not n in rev_graph) or (n in graph and len(graph[n])>1) ]
    
    for n in branches:
        contig = [n]
        cc = graph[n] if n in graph else []
        for c in cc:
            n = c
            contig.append(n)
            cc = graph[n] if n in graph else []
            while len(cc) == 1:
                n = cc[0]
                contig.append(n)
                cc = graph[n] if n in graph else []
                
        
            contigs.append(contig)
    
    contig_string=[]
    for contig in contigs:
        s=contig[0]
        for c in contig[1:]:
            s+=c[-1]
        contig_string.append(s)
    print(",".join(contig_string))
    return contig_string


        
    
    