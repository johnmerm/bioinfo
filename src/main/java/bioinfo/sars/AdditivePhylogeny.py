
def leafLimb(n,D,j):
    mat = [((D[i][j]+D[j][k]-D[i][k])/2,i,k,j) for i in range(n) for k in range(n) if i!=j and j!=k and i !=k]
    return min(mat,key=lambda x:x[0])


def findaPair(D,n):
    for i in range(n-1):
        for k in range(n):
            if k!=i and D[i][k] == D[i][n-1]+D[n-1][k]:
                return (i,k)
    return None


def additivePhylogeny(n,D,labels=None,edges=[],lastLabel=None):
    if labels == None:
        labels = [i for i in range(n)]
    if lastLabel == None:
            lastLabel = n
    if n == 2:
        edges.append((labels[0],labels[1],D[0][1]))
        return edges
    else:
        limbLength = leafLimb(n, D, n-1)
        (i,k) = findaPair(D, n)
        
        x = D[i][n-1]
        y = D[k][n-1]
        newLabel = lastLabel
        lastLabel = lastLabel+1
        
        edges.append((labels[i],newLabel,x))
        edges.append((newLabel,labels[i],x))
        
        edges.append((labels[k],newLabel,y))
        edges.append((newLabel,labels[k],y))
        
        edges.append((labels[n-1],newLabel,limbLength))
        edges.append((newLabel,labels[n-1],limbLength))
        
        DD = [[D[x][y] for y in range(n-1)]for x in range(n-1)]
        
        labels[k] = newLabel
        labels.remove(labels[n-1])
        
        
        additivePhylogeny(n-1, DD, labels, edges,lastLabel)
        return edges
                         

D = [[0,    13,    21,    22],
     [13,    0,    12,    13],
     [21,    12,    0,    13],
     [22,    13,    13,    0]]

edges = additivePhylogeny(4, D)
print sorted(edges,key=lambda x:x[0])

