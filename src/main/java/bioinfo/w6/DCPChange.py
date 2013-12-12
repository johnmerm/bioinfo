'''
Created on Dec 11, 2013

@author: grmsjac6
'''


def dcpChange(money,coins):
    minCoins  = [0]
    for m in range(1,money+1):
        minCoins.append(65535)
        for i in range(len(coins)):
            if m>= coins[i]:
                if minCoins[m-coins[i]]+1<minCoins[m]:
                    minCoins[m] = minCoins[m-coins[i]]+1
    
    return minCoins[m]
    

def manhattanTourist(n,m,down,right):
    s=[[0 for i in range(m+1)]for j in range(n+1)]
    
    for i in range(1,n+1):
        s[i][0] = s[i-1][0]+down[i-1][0]
        
        
    for j in range(1,m+1):
        s[0][j] = s[0][j-1]+right[0][j-1]
    
    for i in range(1,n+1):
        for j in range(1,m+1):
            s[i][j] = max(s[i-1][j]+down[i-1][j],s[i][j-1]+right[i][j-1])
    
    return s[n][m]


def assignment():
    file = open('dataset_72_9.txt')
    
    n=int(next(file))
    m=int(next(file))
    
    str = next(file)
    down=[]
    while str.strip() != "-":
        down.append([int(s) for s in str.strip().split(" ")]  )
        str = next(file)
    
    str = next(file,None)
    right=[]
    while str != None:
        right.append([int(s) for s in str.strip().split(" ")]  )
        str = next(file,None)
    
    mh = manhattanTourist(n, m, down, right)
    
    print(mh)

assignment()
    