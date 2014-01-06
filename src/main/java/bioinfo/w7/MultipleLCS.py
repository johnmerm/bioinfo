'''
Created on Jan 6, 2014

@author: giannis
'''
#It misses initial letters (free ride in front)
def threeSequences(v):
    
    s = [[[0 for k in range(len(v[2])+1)]for j in range(len(v[1])+1)]for i in range(len(v[0])+1)]
    backtrack = [[[7 for k in range(len(v[2]))]for j in range(len(v[1]))]for i in range(len(v[0]))]
    
    
    for i in range(1,len(v[0])+1):
        for j in range(1,len(v[1])+1):
            for k in range(1,len(v[2])+1):
                sb = {}
                sbm = -65535
                bm = 0
                for bitmask in range(1,8):
                    bi = bitmask >> 2
                    bj = (bitmask - (bi<<2)) >> 1
                    bk = (bitmask -(bi<<2) -(bj<<1))
                    score = 1 if ((bi==bj==bk) and (v[0][i-1]==v[1][j-1]==v[2][k-1])) else 0
                    sb[bitmask] = (s[i-bi][j-bj][k-bk] + score)
                    if  sb[bitmask] >sbm:
                        bm = bitmask
                        sbm = sb[bitmask]
                s[i][j][k] = sbm
                backtrack[i-1][j-1][k-1]=bm
    
    
    vv=[[],[],[]]
    i = len(v[0])-1
    j = len(v[1])-1
    k = len(v[2])-1
    
    while i>=0 and j>=0 and k>=0:
        bitmask = backtrack[i][j][k]
        bi = bitmask >> 2
        bj = (bitmask - (bi<<2)) >> 1
        bk = (bitmask -(bi<<2) -(bj<<1))
        
        vv[0].append(v[0][i] if bi == 1 else '-')
        vv[1].append(v[1][j] if bj == 1 else '-')
        vv[2].append(v[2][k] if bk == 1 else '-')
        
        i -= bi
        j -= bj
        k -= bk
    
    vv[0] = ''.join(reversed(vv[0]))
    vv[1] = ''.join(reversed(vv[1]))
    vv[2] = ''.join(reversed(vv[2]))
    
    return s[len(v[0])][len(v[1])][len(v[2])],vv
         