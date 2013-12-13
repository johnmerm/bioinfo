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


def dagOneNode(node,graph,s,backtrack):
    if not node in graph:
        #node == sink
        return 
    connections  = graph[node]
    cs = {c:((s[c] if c in s else 0) + v) for (c,v)  in connections}
    cd = max(cs.items(),key=lambda x:x[1])
    backtrack[cd[0]] = node
    s[node] = cd[1]
    dagOneNode()
     

def dag(source,sink,graph):
    s = {}
    s[source] = 0
    backtrack={}
    dagOneNode(source,graph,s,backtrack)
    
    return s,backtrack
    
    
    
    
def assignment():
    file = open('dataset_74_5.txt')
    out = open('out.txt','w')
    v = next(file)
    w = next(file)
    
    
    out.write(lcs(v, w))
    out.close()

assignment()