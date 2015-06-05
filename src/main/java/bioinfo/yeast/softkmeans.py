import numpy
from math import exp,sqrt
def dist(a,b):
    return sum( [(a[i]-b[i])**2 for i in range(len(a))])

def hColumn(point,centers,stiffness):
    H = [ exp(-stiffness*sqrt(dist(point,c))) for c in centers]
    Hs = sum(H)
    H = [ h/Hs for h in H]
    return H

def hiddenMatrix(Data,Centers,stiffness):
    H = [hColumn(point, Centers, stiffness) for point in Data]
    Hm = numpy.transpose(H);
    return Hm


def dotPoint(a,point):
    return tuple([a*point[i] for i in range(len(point))])


def softKmeans(k,Data,stiffness):
    DataMatrix = numpy.array([ list(d) for d in Data])
    Centers = Data[:k]
    
    for r in range(100):
        H = hiddenMatrix(Data, Centers,stiffness)
        
        for i in range(len(Centers)):
            Hi = numpy.reshape(H[i,:],(1,len(Data)))
            xi = numpy.dot(Hi,DataMatrix) 
            xi_denom = numpy.dot(Hi,numpy.ones((len(Data),1))) 
            xi = xi / xi_denom
            xit = map(tuple,xi)[0]
            Centers[i] = xit
    return Centers
def test_softKmeans():
    k=2
    m=2
    stiffness = 2.7
    Data=[  (1.3, 1.1),
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
            (0.0, 1.9)]
    centers = softKmeans(k, Data,stiffness)
    for center in centers:
        print ' ' .join([str(c) for c in center])

def exam_softKmeans():
    al = list(open('dataset_10933_7.txt'))
    
    k,m = [int(x) for x in al[0].strip().split(' ')]
    stiffness = float(al[1].strip())
    Data = [ tuple([float(x) for x in a.strip().split(' ')]) for a in al[2:] ]
    centers=  softKmeans(k,  Data,stiffness)
    for center in centers:
        print ' ' .join([str(c) for c in center])
if __name__ == '__main__':
    exam_softKmeans()