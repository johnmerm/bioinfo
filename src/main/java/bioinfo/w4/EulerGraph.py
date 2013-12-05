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

def cycle(graph,rev_graph):
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
            n=next(iter(graph.keys()))
        cycle = []
        c = graph[n]
        cycle.append(n)
        while len(c)>0:
            r = n
            n = c[0]
            
            cycle.append(n)
            del c[0]
            c = graph[n]
            
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
