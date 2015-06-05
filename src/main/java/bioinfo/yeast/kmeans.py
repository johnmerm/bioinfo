def pointDist(a,b):
    return sum([(a[i]-b[i])**2 for i in range(len(a))])


def centerOffGravity(points):
    m = len(next(iter(points)))
    return tuple([sum([d[i] for d in points])/len(points) for i in range(m)])  
def dist(a,centers):
    d = {b:pointDist(a,b) for b in centers}
    dm = min(d.items(),key = lambda x:x[1])
    return dm[1]




def farthestFirstTraversal(Data, k,scoring = dist):
    dataPoint =  Data[0]
    centers = {dataPoint}
    while len(centers)<k:
        dataPoint = max(Data,key = lambda x:scoring(x,centers))
        centers.add(dataPoint)
    return centers
         

def distortion(Data,k,centers):
    n = len(Data)
    dm =[dist(a,centers) for a in Data]
    return sum(dm)/n

def test_farthestFirstTraversal():
    k=3
    Data = [(0.0, 0.0),
            (5.0, 5.0),
            (0.0, 5.0),
            (1.0, 1.0),
            (2.0, 2.0),
            (3.0, 3.0),
            (1.0, 2.0)]
    centers = farthestFirstTraversal(Data, k)
    print centers


def test_distortion():
    k=2
    centers = {(2.31,4.55),(5.96,9.08)}
    Data = [(3.42, 6.03),
            (6.23, 8.25),
            (4.76, 1.64),
            (4.47, 4.33),
            (3.95, 7.61),
            (8.93, 2.97),
            (9.74, 4.03),
            (1.73, 1.28),
            (9.72, 5.01),
            (7.27, 3.77)
            ]
    
    print distortion(Data, k, centers)
    


def lloydStep(Data,centers):
    clusters = {}
    for dataPoint in Data:
        cluster = min(centers,key = lambda center:pointDist(dataPoint, center))
        if cluster in clusters:
            clusters[cluster].add(dataPoint)
        else:
            clusters[cluster] = {dataPoint}
    
    moves = {}
    dists = {}
    for c,dc in clusters.items():
        cn = centerOffGravity(dc)
        moves[c] = cn
        dists[c] = pointDist(c, cn)
    return moves,dists


def lloyd(data,k):
    centers = {c for c in data[:k]}
    moves,dists = lloydStep(data, centers)
    while(sum(dists.values())>0.000001):
        centers = moves.values()
        moves,dists = lloydStep(data, centers)
    return moves.values()

def test_lloyd():
    k = 2
    Data = [(1.3, 1.1),
            (1.3, 0.2),
            (0.6, 2.8),
            (3.0, 3.2),
            (1.2, 0.7),
            (1.4, 1.6),
            (1.2, 1.0),
            (1.2, 1.1),
            (0.6, 1.5),
            (1.8, 2.6),
            (1.2, 1.3),
            (1.2, 1.0),
            (0.0, 1.9)
            ]
    centers = lloyd(Data, k)
    
    for c in centers:
        print ' '.join([str(e) for e in c])
        
        
def exam_lloyd():
    al = list(open('dataset_10928_3.txt'))
    k,m = [int(x) for x in al[0].strip().split(' ')]
    Data = [ tuple([float(x) for x in a.strip().split(' ')]) for a in al[1:] ]
    
    centers = lloyd(Data,k)
    for c in centers:
        print ' '.join([str(e) for e in c])
        
def exam_farthestFirstTraversal():
    al = list(open('dataset_10926_14.txt'))
    k,m = [int(x) for x in al[0].strip().split(' ')]
    Data = [ tuple([float(x) for x in a.strip().split(' ')]) for a in al[1:] ]
    centers = farthestFirstTraversal(Data, k)
    for c in centers:
        print ' '.join([str(e) for e in c])
        
def exam_distortion():
    al = list(open('dataset_10927_3.txt'))
    k,m = [int(x) for x in al[0].strip().split(' ')]
    splitpoint = al.index('--------\n')
    centers = {tuple([float(x) for x in a.strip().split(' ')]) for a in al[1:splitpoint] }
    Data = [ tuple([float(x) for x in a.strip().split(' ')]) for a in al[splitpoint+1:] ]
    print distortion(Data, k, centers)
    
if __name__ == '__main__':
    exam_lloyd()
     
    
    