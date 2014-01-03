'''
Created on Jan 3, 2014

@author: giannis
'''

from bioinfo.w6.Allignment import blosum62
from numpy.ma.core import ceil

def middleEdge(v,w,sigma = 5):
    
    n = len(v)
    m = len(w)
    m_mid = int(ceil(m/2))
    
    s = [-sigma*i for i in range(n)]
    
    
    for j in range(1,m_mid+1):
        s_back = s
        s = [0 for i in range(n) ]
        for i in range(1,n):
            sg = s_back[i-1] + blosum62[(v[i-1],w[j-1])]
            sd = s[i-1] - sigma
            sr = s_back[i] - sigma
            s[i] = max(sg,sd,sr)
    
    
    sm = -65535
    smi = 0
    
    for i in range(n):
        if s[i]>sm:
            sm = s[i]
            smi = i
    
    x = (smi,j)
    s_back = s
    for i in range(1,n):
        sg = s_back[i-1] + blosum62[(v[i-1],w[j-1])]
        sd = s[i-1] - sigma
        sr = s_back[i] - sigma
        s[i] = max(sg,sd,sr)
    
    sd = s_back[smi+1]
    sr = s[smi]
    sg = s[smi+1]
    
    s_max = max(sd,sg,sr)
    if s_max == sd:
        y = (smi+1,j)
    elif s_max == sr:
        y = (smi,j+1)
    else:
        y= (smi+1,j+1)
    
    

    return x,y