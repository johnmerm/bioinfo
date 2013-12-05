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

def cycle(graph,rev_graph,n=None):
    bigcycle=[]
    while sum([len(a) for a in graph.values()]) >0 :
        
        if len(bigcycle) >0:
            n = None
            for i in graph.keys():
                if len(graph[i]) >0 and len(rev_graph[i]) >0 and i in bigcycle:
                    n = i
                    break
            if n == None:
                raise NameError('Graph exhausted')
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

def pathToCycle(graph,rev_graph):
    oddNodes = []
    allNodes = set(graph.keys()).union(rev_graph.keys())
    
    for n in allNodes:
        out = graph[n] if n in graph else []
        inc = rev_graph[n] if n in rev_graph else []
        s = len(out)+len(inc)
        if s % 2 == 1:
            oddNodes.append(n)
    
    if len(oddNodes) == 0:
        return None
    elif len(oddNodes) % 2 ==0:
        noOutgoinConn = {n for n in allNodes if not n in graph}
        noIncomingConn =  {n for n in allNodes if not n in rev_graph}
        unbalanced = {n for n in oddNodes if n in graph and n in rev_graph}
        disconnected = {n for n in allNodes if not n in graph and not n in rev_graph}
        
        nic = iter(noIncomingConn)
        for n in noOutgoinConn:
            c = next(nic)
            graph
        return oddNodes
            
    else:
        raise NameError('Graph has '+str(len(oddNodes))+' unbalanced nodes')
            
        
    
    
    