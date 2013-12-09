'''
Created on Dec 9, 2013

@author: grmsjac6
'''
from EulerGraph import connect, paths, copyGraph


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
    k = len(path[0][0])+1
    
    string = path[0][0]
    string_d = path[0][1]
    for ps in path[1:]:
        sf = ps[0][-1]
        sf_d = ps[1][-1]
        string+=sf
        string_d+=sf_d
    
    
    for i in range(len(string)-d-k):
        s = string[i+d+k]
        sd =  string_d[i]
        if s !=sd:
            return None
    
    string_prefix = string[:k+d]
    return string_prefix+string_d



    
def pairedReads(lines,d):
    graph,rev_graph = pairedDeBru(lines)
    
    c_g = copyGraph(graph)
    c_r = copyGraph(rev_graph)
    path = paths(c_g, c_r)
    string  = validatePath(path, d)    
    while string == None:
        c_g = copyGraph(graph)
        c_r = copyGraph(rev_graph)
        path = paths(c_g, c_r)
        string  = validatePath(path, d)
    return string

def assignment():
    file = open('/home/giannis/Downloads/dataset_58_14.txt')
    data =list(file)
    file.close()
    d= int(data[0])
    lines = [d.strip() for d in data[1:]]
    string = pairedReads(lines, d)
    out_file = open('out_file.txt','w')
    out_file.write(string)
    out_file.close()
    return string    

print(assignment())