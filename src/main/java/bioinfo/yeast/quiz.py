'''
Created on May 26, 2015

@author: grmsjac6
'''
from math import sqrt
import numpy
def pointDist(a,b):
    return sum([(a[i]-b[i])**2 for i in range(len(a))])


def test_maxDist():
    points = [(2, 6), (4, 9), (5, 7), (6, 5), (8, 3) ]
    centers = [ (4, 5), (7, 4)]
    
    dists = [[sqrt(pointDist(p, c)) for c in centers] for p in points]
    
    minDists = [min(dists[i]) for i in range(len(points))]
    
    maxDist = max(minDists)
    return maxDist


def test_distrortion():
    points = [ (2, 6), (4, 9), (5, 7), (6, 5), (8, 3) ] 
    centers =[ (4, 5), (7, 4) ]
    
    dists = [[pointDist(p, c) for c in centers] for p in points]
    
    minDists = [min(dists[i]) for i in range(len(points))]
    
    distortion = sum(minDists)/len(points)
    return distortion
    
def centerOffGravity(points,m):
    return tuple([sum([d[i] for d in points])/len(points) for i in range(m)])  
def test_centerOfGravity():
    points = [(17, 0, -4), (3, 14, 23), (9, 7, 16), (7, 3, 5)]
    return centerOffGravity(points, 3)



def hColumn(point,centers,stiffness):
    H = [ 1.0/(pointDist(point,c)) for c in centers]
    Hs = sum(H)
    H = [ h/Hs for h in H]
    return H

def hiddenMatrix(Data,Centers,stiffness):
    H = [hColumn(point, Centers, stiffness) for point in Data]
    Hm = numpy.transpose(H);
    return Hm

def test_hiddenMatrix():
    Data =[ (2,8), (2,5), (6,9), (7,5), (5,2)]
    Centers =[(3,5), (5,4)]
    print hiddenMatrix(Data, Centers, None)
    
def test_weightCenterOfgravity():
    Data =[ (2,6), (4,9), (5,7), (6,5), (8,3)]
    DataMatrix = numpy.array([ list(d) for d in Data])
    
    i=0
    H = numpy.array([[0.5, 0.3, 0.8, 0.4, 0.9],
                     [0.5, 0.7, 0.2, 0.6, 0.1]])
    
    Hi = numpy.reshape(H[i,:],(1,len(Data)))
    xi = numpy.dot(Hi,DataMatrix) 
    xi_denom = numpy.dot(Hi,numpy.ones((len(Data),1))) 
    xi = xi / xi_denom
    xit = map(tuple,xi)[0]
    
    print xit
    
if __name__ == '__main__':
    print test_weightCenterOfgravity()