'''
Created on Jan 3, 2014

@author: giannis
'''

from bioinfo.w6.Allignment import blosum62


def backtrackstring(v,w,s,backtrack):
    n = len(v)
    m = len(w)
    
    i = n-1
    j = m-1
    
    vv=[]
    ww=[]
    while i>=0 and j>=0:
        if backtrack[i][j] == 'g':
            vv.append(v[i])
            ww.append(w[j])
            i-=1
            j-=1
        elif backtrack[i][j] == 'd':
            vv.append(v[i])
            ww.append("-")
            i-=1
        elif backtrack[i][j] == 'r':
            vv.append("-")
            ww.append(w[j])
            j-=1
                
    return s[n][m],''.join(reversed(vv)),''.join(reversed(ww))

def affineAllign(v,w,epsilon = 1,sigma = 11):
    n = len(v)
    m=  len(w)
    
    s_low = [[0 for j in range(m+1)] for i in range(n+1)]
    s_mid = [[0 for j in range(m+1)] for i in range(n+1)]
    s_up = [[0 for j in range(m+1)] for i in range(n+1)]
    
    backtrack=[['' for j in range(m)] for i in range(n)]
    
    for i in range(1,n+1):
        for j in range(1,m+1):
            s_low[i][j] = max(s_low[i-1][j] - epsilon,s_mid[i-1][j] - sigma)
            s_up[i][j] = max(s_up[i][j-1] - epsilon,s_mid[i][j-1] - sigma)
            
            sd = s_low[i][j]
            sr = s_up[i][j]
            sg = s_mid[i-1][j-1] + blosum62[(v[i-1],w[j-1])]
            
            s_mid[i][j] = max(sd,sr,sg)
            
            if s_mid[i][j] == sd:
                backtrack[i-1][j-1]='d'
            elif s_mid[i][j] == sr:
                backtrack[i-1][j-1] = 'r'
            else:
                backtrack[i-1][j-1] = 'g'
            
    
    return backtrackstring(v, w, s_mid, backtrack)