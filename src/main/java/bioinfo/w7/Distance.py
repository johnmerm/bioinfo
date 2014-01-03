'''
Created on Dec 20, 2013

@author: giannis
'''

def distance(v,w):
    n = len(v)
    m = len(w)
    s= [[0 for j in range(m+1)] for i in range(n+1)]
    backtrack=[['' for j in range(m)] for i in range(n)]
    
    for i in range(n):
        s[i+1][0]=s[i][0]+1
#         backtrack[i][0] = 'd'
    for j in range(m):
        s[0][j+1]= s[0][j]+1
#         backtrack[0][j] = 'r'
    
    for i in range(1,n+1):
        for j in range(1,m+1):
            sg = s[i-1][j-1] + (0 if v[i-1]==w[j-1] else 1)
            sd = s[i-1][j] + 1
            sr = s[i][j-1] + 1
            s[i][j] = min(sg,sd,sr)
            if s[i][j] == sg: 
                backtrack[i-1][j-1] = 'g'  
            elif  s[i][j] == sd: 
                backtrack[i-1][j-1] = 'd' 
            else : 
                backtrack[i-1][j-1] = 'r'
    
    i= n-1
    j=m-1
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




def fitting (v,w,penalty=1):
    
    n = len(v)
    m = len(w)
    s= [[0 for j in range(m+1)] for i in range(n+1)]
    backtrack=[['' for j in range(m)] for i in range(n)]
    
    for i in range(n):
        #fitting is like local assignment where free rides occur only in the vertical direction
        s[i+1][0]= 0
         
    for j in range(m):
        #initial moving right is penalized as usual
        s[0][j+1]= s[0][j]-penalty

    for i in range(1,n+1):
        for j in range(1,m+1):
            sg = s[i-1][j-1] + (1 if v[i-1]==w[j-1] else -penalty)
            sd = s[i-1][j] - (penalty if j!=m else 0) # ending moves down are free
            sr = s[i][j-1] - penalty
            s[i][j] = max(sg,sd,sr)
            if s[i][j] == sg: 
                backtrack[i-1][j-1] = 'g'  
            elif  s[i][j] == sd: 
                backtrack[i-1][j-1] = 'd' 
            else : 
                backtrack[i-1][j-1] = 'r'
    i=n-1
    j=m-1
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
    
def overlap(v,w,penalty = 2):
    n = len(v)
    m = len(w)
    
    s= [[0 for j in range(m+1)] for i in range(n+1)]
    backtrack=[['' for j in range(m)] for i in range(n)]
    
    
    for i in range(n):
        s[i+1][0]= 0
         
    for j in range(m):
        ##when  overlapping initial moves to the right are allowed
        s[0][j+1]= s[0][j]-penalty

    for i in range(1,n+1):
        for j in range(1,m+1):
            sg = s[i-1][j-1] + (1 if v[i-1]==w[j-1] else -penalty)
            sd = s[i-1][j] - penalty 
            sr = s[i][j-1] - (penalty if i!=n else 0) #right ending moves are free
            s[i][j] = max(sg,sd,sr)
            if s[i][j] == sg: 
                backtrack[i-1][j-1] = 'g'  
            elif  s[i][j] == sd: 
                backtrack[i-1][j-1] = 'd' 
            else : 
                backtrack[i-1][j-1] = 'r'
    i=n-1
    j=m-1
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
            
def assignment():
    f = open('dataset_77_3.txt')
    v = next(f).strip()
    w = next(f).strip()
    
    d,vv,ww = overlap(v, w)
    print(d)
    print(vv)
    print(ww)
    return d,vv,ww
#assignment()