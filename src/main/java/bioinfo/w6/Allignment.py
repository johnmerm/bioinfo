'''
Created on Dec 16, 2013

@author: grmsjac6
'''

from LCS import lcs,dag,calculateDags



def loadMatrix(f):
    matrix={}
    mat_file = open(f)
    head_line = next(mat_file)
    headers = head_line.strip().split()
    for line in mat_file:
        toks = line.strip().split()
        pivot = toks[0]
        for i in range(1,len(toks)):
            colname = headers[i-1]
            matrix[(pivot,colname)] = int(toks[i])
    return matrix

def globalAlign(v,w,sigma=5):
    m = loadMatrix('BLOSUM62.txt')
    s,backtrack,r =  lcs(v, w, 5, lambda x,y:m[(x,y)])
    
    i = len(v)
    j = len(w)
    
    vv = []
    ww = []
    while i>0 or j >0:
        b = backtrack[i][j]
        print(b)
        if b == 'd':
            i = i-1
            vv.append(v[i])
            ww.append("-")
            
            
           
            
        elif b =='r':
            j = j-1
            ww.append(w[j])
            vv.append("-")
            
            
            
        else:
            i = i-1
            j=j-1
            vv.append(v[i])
            ww.append(w[j])
            
            
            
    return s,''.join(reversed(vv)),''.join(reversed(ww))
     
 
def assignmentGlobal():
    f = open('dataset_76_3.txt')
    v=  next(f).strip()
    w = next(f).strip()
    
    s,o,u = globalAlign(v, w)
    print(s)
    print(o)
    print(u)
    


def localAllign(v,w,sigma=5):
    m = loadMatrix('PAM250_1.txt')
    s,backtrack,r =  lcs(v, w, 0, lambda x,y:m[(x,y)])
    
    i = len(v)
    j = len(w)
    
    vv = []
    ww = []
    while i>0 or j >0:
        b = backtrack[i][j]
        print(b)
        if b == 'd':
            i = i-1
            vv.append(v[i])
            ww.append("-")
            
            
           
            
        elif b =='r':
            j = j-1
            ww.append(w[j])
            vv.append("-")
            
            
            
        else:
            i = i-1
            j=j-1
            vv.append(v[i])
            ww.append(w[j])
            
            
            
    return s,''.join(reversed(vv)),''.join(reversed(ww))
    

def createDAG(v,w,mat,sigma=5):
    graph={}
    for i in range(len(v)):
        for j in range(len(w)):
            node = str(i)+','+str(j)
            
            graph[node]=[]
            if i<len(v) and j <len(w):
                node_diag = str(i+1)+','+str(j+1)
                graph[node].append((node_diag,mat[(v[i],w[j])]))
            
            if i<len(v):
                node_down = str(i+1)+','+str(j)
                graph[node].append((node_down,-sigma))
            
            if j<len(w): 
                node_right = str(i)+','+str(j+1)
                graph[node].append((node_right,-sigma))
    return graph

def movement(p_this,p_next):
    n_this = [int(a) for a in p_this.split(",")]
    n_next = [int(a) for a in p_next.split(",")]
    
    if n_this[0] == n_next[0] and n_next[1] == n_this[1]+1:
        return 'r'
    elif n_next[0] == n_this[0]+1 and n_next[1] == n_this[1]:
        return 'd'
    elif n_next[0] == n_this[0]+1 and n_next[1] == n_this[1]+1:
        return 'g'
    else:
        return 'f'
    
def allignDAG(v,w,local=False):
    mat = loadMatrix('BLOSUM62.txt')
    graph = createDAG(v, w, mat, 5)
    print(len(graph))
    source = '0,0'
    sink = str(len(v))+','+str(len(w))
    
    if local:
        for node in graph:
            graph[source].append((node,0))
            graph[node].append((sink,0))
        
        print(len(graph))
    
    s, path = dag(source,sink , graph)
            
    vv=""
    ww=""
    i=0
    j=0
    
    for p in range(len(path)-1):
        p_this = path[p]
        p_next = path[p+1]
        mvmt = movement(p_this, p_next)
        if mvmt=='d':
            vv+=v[i]
            ww+="-"
            i+=1
        elif mvmt=='r':
            vv+="-"
            ww+=w[j]
            j+=1
            
        elif mvmt=='g':
            vv+=v[i]
            ww+=w[j]
            
            i+=1
            j+=1
    
#     vv+=v[i]
#     ww+=w[j]
#     s+= mat[(v[i],w[j])]
    return s,vv,ww
            
            
                
def localDag(v,w,sigma,mat):
    graph={}
    rev_graph = {}
     
    for i in range(len(v)):
        for j in range(len(w)):
            node = str(i)+','+str(j)
            
            graph[node]=[]
            if i<len(v) and j <len(w):
                node_diag = str(i+1)+','+str(j+1)
                graph[node].append((node_diag,mat[(v[i],w[j])]))
            
            if i<len(v):
                node_down = str(i+1)+','+str(j)
                graph[node].append((node_down,-sigma))
            
            if j<len(w): 
                node_right = str(i)+','+str(j+1)
                graph[node].append((node_right,-sigma))
    return graph
    
    
    
       
     
    
     