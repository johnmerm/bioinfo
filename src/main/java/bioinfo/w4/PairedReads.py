'''
Created on Dec 9, 2013

@author: grmsjac6
'''
from bioinfo.w4.EulerGraph import connect, paths
from bioinfo.w4.StringReconstruction import StringReconstruction

def pairedDeBru(lines):
    graph = {}
    rev_graph={}
    
    for line in lines:
        l = line.strip().split("|")
        pref = (l[0][:-1],l[1][:-1])
        suff = (l[0][1:],l[1][1:])
        
        connect(pref,suff,graph,rev_graph)
    
    return graph,rev_graph

def validatePath(path,d):
    string = path[0][0]
    string_d = path[0][1]
    for ps in path[1:]:
        sf = ps[0][-1]
        sf_d = ps[1][-1]
        string+=sf
        string_d+=sf_d
    
    for i in range(len(string)):
        s = string[(i+d)%len(string)]
        sd =  string_d[i]
        if s !=sd:
            return None
    return string
    
    
    
     
    
        
def pairedReads(lines,d):
    graph,rev_graph = pairedDeBru(lines)
    c_g = {x:list(v) for (x,v) in graph.items()}
    c_r = {x:list(v) for (x,v) in rev_graph.items()}
    pt = paths(c_g, c_r)
    string = validatePath(pt, d)
    while string == None:
        c_g = {x:list(v) for (x,v) in graph}
        c_r = {x:list(v) for (x,v) in rev_graph}
        pt = paths(c_g, c_r)
        string = validatePath(pt, d)
    
    return string
