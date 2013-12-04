from timeit import itertools
from random import randint

def parseGraph(lines):
    graph = {}
    
    for line in lines:
        toks = line.split(" -> ")
        graph[toks[0]]=toks[1].strip().split(",")
        
    rev_graph = {}
    
    for (n,cc) in graph.items():
        for c in cc:
            if c in rev_graph:
                rev_graph[c].append(n)
            else:
                rev_graph[c] = [n]
    return (graph,rev_graph)

def copyGraph(graph):
    return {k:list(v) for k,v in graph.items() }

acl=0

def eulerCycles(graph,cycle=[],n=None,cycles=[]):
    cg = copyGraph(graph)
    if n == None:
        n = list(cg.keys())[randint(0,len(cg)-1)]
    
    startN = cycle[0] if len(cycle)>0 else n
    
    if len(cycles)==0:
        cycles.append(cycle)
    
    while True:
        cycle.append(n)
        connections = cg[n]
        
        if len(connections) == 0:
            if (n == startN and len(cycle) == acl+1):
                print (" -> ".join(cycle))
            break
        elif len(connections) >1:
            cycles.remove(cycle)
            for ni in connections:
                cgi = copyGraph(cg)
                thisCycle = list(cycle)
                cycles.append(thisCycle)
                cgi[n].remove(ni)
                eulerCycles(cgi, thisCycle, ni, cycles)
            break
        else:
            ni = connections[0]
            cg[n].remove(ni)
            n = ni
    return cycles
    
def allLinesinGraph(graph,rev_graph):
    cg = list(graph.items())
    
    
    allLines=[]
    for (n,c) in cg:
        line = []
        #forward search
        while True:
            if len(c)==1:
                line.append(n)
                if (n,c) in cg:
                    cg.remove((n,c)) 
                    n = c[0]
                    c = graph[n]
                else:
                    break
            elif len(c)>1:
                line.append(n)
                break
            
        if len(line) >0:
            #go backwards
            n = line[0]
            c = rev_graph[n]
            while len(c) ==1:
                n = c[0]
                c = rev_graph[n]
                line = [n]+line
                cg.remove((n,c))
                
        allLines.append(line)
            
    return allLines
        

data = list(open('C:/Users/grmsjac6.GLOBAL-AD/Downloads/dataset_57_2.txt'))
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

#lines = data

graph,rev_graph = parseGraph(lines)

# allLines = allLinesinGraph(graph,rev_graph)
# for l in allLines:
#     print(" -> ".join(l))
# print("_______________________________________________")    


print("\n".join([" -> ".join(g) for g in eulerCycles(graph)]))