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

def cycle(graph,rev_graph,start=None):
    bigcycle=[]
    if start != None:
        n = start
    else:
        n = None
        
    while sum([len(a) for a in graph.values()]) >0 :
        
        if len(bigcycle) >0:
            n = None
            cands = []
            for i in graph.keys():
                a =len(graph[i]) if i in graph else 0
                b = len(rev_graph[i]) if i in rev_graph else 0  
                if  a>0 and b>0 and i in bigcycle:
                    cands.append(i)
#                     if len(cands)==1:
#                         break
            
            if len(cands)>0:
                n = cands[randint(0,len(cands)-1)]    
            else:
                print('Graph exhausted')
                break
        else:
            if n == None:
                n=next(iter(graph.keys()))
        cycle = []
        c = graph[n]
        cycle.append(n)
        while len(c)>0:
            r = n
            n = c[0]
            
            cycle.append(n)
            del c[0]
            c = graph[n] if n in graph else []
            
            cr = rev_graph[n] 
            cr.remove(r)
            
        if len(bigcycle) == 0:
            bigcycle = cycle
        else:
            ind = bigcycle.index(cycle[0])
            prefix = bigcycle[:ind]
            suffix = bigcycle[ind+1:]
            bigcycle = prefix+cycle+suffix
            
    return bigcycle

def preparePath(graph,rev_graph):
    oddNodes = {}
    allNodes = set(graph.keys()).union(rev_graph.keys())
    
    for n in allNodes:
        out = graph[n] if n in graph else []
        inc = rev_graph[n] if n in rev_graph else []
        s = len(out)-len(inc)
        if s != 0:
            oddNodes[n] = s
    
    if len(oddNodes) == 0:
        return None
    else: 
        oddNodes = sorted(oddNodes.items(),key=lambda x:x[1])
        return oddNodes    
def connect(a,b,graph,rev_graph):
    if a in graph:
        graph[a].append(b)
    else:
        graph[a] = [b]
    
    if b in rev_graph:
        rev_graph[b].append(a)
    else:
        rev_graph[b] = [a]

def paths(graph,rev_graph):
    paths = []
    oddNodes = preparePath(graph, rev_graph)
    
    
    if oddNodes == None:
        return cycle(graph, rev_graph,None)
    else:
        g = dict(graph)
        r = dict(rev_graph)
        while oddNodes != None:
            o = oddNodes[0]
            i = oddNodes[-1]
            if len(oddNodes) ==2:
                break
            else:
                connect(o[0],i[0],g,r)
                oddNodes = preparePath(g, r)
                
        start = i[0]
        path = cycle(g, r, start)
#        print("->".join(path))
        return path
    