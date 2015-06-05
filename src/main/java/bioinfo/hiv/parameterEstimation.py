'''
Created on Jun 5, 2015

@author: grmsjac6
'''
from symtable import Symbol


def parameterEstimation(x,alphabet,path,symbols):
    trans = {}
    ems = {}
    for i in range(len(x)):
        p = path[i]
        a = x[i]
        
        if not p in ems: ems[p] = {}
        
        if a in ems[p]: ems[p][a] +=1
        else :ems[p][a] = 1
    
    sum_ems = {p:sum(v.values()) for (p,v) in ems.items()}
    norm_ems = {p:{vk:float(vv)/sum_ems[p] for (vk,vv) in v.items()} for (p,v) in ems.items()}
    
    for i in range(len(path)-1):
        _f = path[i]
        _t = path[i+1]
        
        if not _f in trans: trans[_f] = {}
        
        if _t in trans[_f]: trans[_f][_t] += 1
        else: trans[_f][_t] = 1
    
    sum_trans = {p:sum(v.values()) for (p,v) in trans.items()}
    norm_trans = {p:{vk:float(vv)/sum_trans[p] for (vk,vv) in v.items()} for (p,v) in trans.items()}
    
    trans_mat = [[norm_trans[_f][_t] if _t in norm_trans[_f] else 0 for _t in symbols]
                 if _f in norm_trans else [1./len(symbols) for _t in symbols] 
                 for _f in symbols] 
    ems_mat = [[norm_ems[_f][_t] if _t in norm_ems[_f] else 0 for _t in alphabet]
               if _f in norm_ems else [1./len(alphabet) for _t in alphabet] 
               for _f in symbols]
    
    return trans_mat,ems_mat


def printMatrices(trans_mat,ems_mat,symbols,alphabet):
    print ' \t'+'\t'.join(symbols)
    for i in range(len(symbols)):
        print symbols[i]+'\t'+'\t'.join([str(t) for t in 
                                       trans_mat[i]])
    print "--------"
    
    print ' \t'+'\t'.join(alphabet)
    for i in range(len(symbols)):
        print symbols[i]+'\t'+'\t'.join([str(t) for t in 
                                      ems_mat[i]])

def test_parameterEstimation():
    lines = ['yzzzyxzxxx','--------','x y z','--------','BBABABABAB','--------','A B C']
    x = lines[0].strip()
    alphabet = lines[2].strip().split()
    path = lines[4].strip()
    symbols = lines[6].strip().split()
    trans_mat,ems_mat = parameterEstimation(x, alphabet, path, symbols) 
    
    printMatrices(trans_mat, ems_mat, symbols, alphabet)
    


def exam_parameterEstimation():
    lines = list(open('dataset_11632_8.txt'))
    
    x = lines[0].strip()
    alphabet = lines[2].strip().split()
    path = lines[4].strip()
    symbols = lines[6].strip().split()
    trans_mat,ems_mat = parameterEstimation(x, alphabet, path, symbols) 
    
    
    printMatrices(trans_mat, ems_mat, symbols, alphabet)  

if __name__ == '__main__':
    exam_parameterEstimation()