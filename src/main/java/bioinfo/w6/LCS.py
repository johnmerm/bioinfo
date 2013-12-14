'''
Created on Dec 13, 2013

@author: grmsjac6
'''
def lcs(v,w):
    n = len(v)
    m = len(w)
    
    s=[[0 for i in range(m+1)]for j in range(n+1)]
    backtrack=[['' for i in range(m+1)]for j in range(n+1)]
    
    for i in range(1,n+1):
        for j in range(1,m+1):
            d = s[i-1][j]
            r = s[i][j-1]
            g = s[i-1][j-1]+1 if v[i-1] == w[j-1] else 0
            
            s[i][j] = max(d,r,g)
            
            
            if s[i][j] == d:
                backtrack[i][j] = 'd'
            elif s[i][j] == r:
                backtrack[i][j] ='r'
            elif s[i][j] == g:
                backtrack[i][j] = 'g'
            
    return outputLCS(backtrack, v, i, j)

def outputLCS(backtrack,v,ii,jj):
    i = ii
    j = jj
    out = []
    
    while i>0 and j >0:
        b = backtrack[i][j]
        print(b)
        if b == 'd':
            i = i-1
        elif b =='r':
            j = j-1
        else:
            
            i = i-1
            j=j-1
            out.append(v[i])
            
           
    return ''.join(reversed(out))


     

def calculateDags(node,graph,s,l,backtrack):
    if node in graph:
        sb = s[node]
        lb = l[node]
        
        connections  = graph[node]
        for (c,v) in connections:
            sa = sb + v
            if not c in s:
                s[c] = sa
                backtrack[c] = node
            elif sa>s[c]:
                s[c] = sa
                backtrack[c] = node
                
            l[c] = lb+1
            calculateDags(c, graph, s,l,backtrack)

def dag(source,sink,graph):
    s = {source:0}
    l={source:0}
    backtrack = {}
    calculateDags(source, graph, s,l,backtrack)
    
    rev_graph = {}
    for n,cc in graph.items():
        cns = [g for (g,v) in cc]
        for c in cns:
            if c in rev_graph:
                rev_graph[c].append(n)
            else:
                rev_graph[c] = [n]
    
    node = sink
    path = []
    w = 0
    while node != source:
        path.append(node)
        node_next = backtrack[node]
#         cns = rev_graph[node]
#         node_next = max(cns,key=lambda x:l[x] if x in l else 0)
        wv = filter(lambda x:x[0] == node, graph[node_next])
        w += wv[0][1]
        node = node_next
    path.append(node)
    return w,reversed(path)

def assignmentDAG():
    f = open('/home/giannis/Downloads/dataset_74_7.txt')
   
    source = next(f).strip()
    sink = next(f).strip()
    lines = [l.strip() for l in f]
    
    graph = {}
    for line in lines:
        toks = line.split("->")
        key = toks[0]
        value = toks[1].split(":")
        vv = (value[0], int(value[1])) 
        if key in graph:
            graph[key].append(vv)
        else:
            graph[key] = [vv]
         
    w, path = dag(source, sink, graph)
    print(w)
    print("->".join(path)) 
    
    
    
    
    
def assignment():
    file = open('dataset_74_5.txt')
    out = open('out.txt','w')
    v = next(file)
    w = next(file)
    
    
    out.write(lcs(v, w))
    out.close()

assignmentDAG()
