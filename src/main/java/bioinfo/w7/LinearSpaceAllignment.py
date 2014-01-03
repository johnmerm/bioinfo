'''
Created on Jan 3, 2014

@author: giannis
'''

def middleNode(v,w,top,bottom,left,right):
    pass

def middleEdge(v,w,top,bottom,left,right):
    pass

def linearSpaceAllignment(v,w):
    top = 0
    left = 0
    bottom = len(v)
    right = len(w)
    edges = []
    while left !=right:
        middle = int((left+right)/2)
        midNode = middleNode(v, w, top, bottom, left, right)
        midEdge = middleEdge(v, w, top, bottom, left, right)
        
        edges.append(midEdge)
        bottom = midNode
        right = middle
    
    
    
    pass

