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
        
       
    
    
    
            
    
                
                