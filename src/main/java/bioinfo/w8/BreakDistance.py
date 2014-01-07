'''
Created on Jan 7, 2014

@author: grmsjac6
'''


def appendToGraph(graph,n,c):
    if n in graph:
        graph[n].append(c)
    else:
        graph[n] = [c]

def breakDistance(genomes):
    graph = {}
    for genome in genomes:
        for part in genome:
            for i in range(len(part)):
                p_this = part[i]
                p_prev = part[i-1]
                appendToGraph(graph, p_prev, -p_this)
                appendToGraph(graph, -p_this, p_this)
    
    
    
            
    
                
                