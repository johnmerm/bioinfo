'''
Created on Jan 9, 2014

@author: grmsjac6
'''
from cProfile import label

class Node(object):
    def __init__(self,id,label):
        self.id = id
        self.label  = label
        self.children = {}
    def addChild(self,id,child):
        childNode = Node(id,child) 
        self.children[child] = Node(id,child) 
        return childNode
    def __str__(self):
        return "%d:%s %s" %(self.id,self.label,",".join(self.children.values()))
    
        
    
def Trie(patterns):
    idx = 1
    root = Node(idx,None)
    for pattern in patterns:
        pNode = root
        for p in pattern:
            if p in pNode.children:
                pNode = pNode.children[p]
            else:
                idx +=1
                pNode = pNode.addChild(idx, p)
    return root

def printTrie(trie,id=None): 
    if trie.label != None:
        print("%d %d %s" % (id,trie.id,trie.label))
    
    for c in trie.children.values():
        printTrie(c,trie.id)
    
                
    