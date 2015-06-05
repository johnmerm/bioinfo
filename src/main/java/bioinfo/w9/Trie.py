'''
Created on Jan 9, 2014

@author: grmsjac6
'''


class Node(object):
    def __init__(self,nid,parent,label):
        self.nid = nid
        self.parent = parent
        self.label  = label
        self.children = {}
    def recstr(self):
        v=self
        m = []
        while v.label != None:
            m.append(v.label)
            v= v.parent
        return ''.join(reversed(m))
    def __str__(self):
        s=''
        if self.label != None:
            s = s+self.label
        if self.nid !=None:
            s = s+'('+str(self.nid)+')'
        return s
            
        
    
def Trie(patterns):
    idx = 1
    root = Node(idx,None,None)
    for pattern in patterns:
        pNode = root
        for p in pattern:
            if p in pNode.children:
                pNode = pNode.children[p]
            else:
                idx +=1
                childNode = Node(idx,pNode,p)
                pNode.children[p] = childNode
                pNode = childNode
    return root

def printTrie(trie,id=None): 
    if trie.label != None:
        print("%d %d %s" % (id,trie.id,trie.label))
    
    for c in trie.children.values():
        printTrie(c,trie.id)

def prefixTrieMatching(text,trie):
    v = trie
    for p in text:
        if p in v.children:
            v = v.children[p]
            if len(v.children) == 0:
                return v
        else:
            return None
    return None

def trieMatching(text,patterns):
    trie = Trie(patterns)
    m={}
    for i in range(len(text)):
        s_text = text[i:]
        v = prefixTrieMatching(s_text, trie)
        if v!=None:
            mm=[]
            while v.label != None:
                mm.append(v.label)
                v = v.parent
            p = ''.join(reversed(mm))
            if p in m:
                m[p].append(i)
            else:
                m[p] = [i]
    return m

def SuffixTrie(text):
    root = Node(None,None,None)
    #build trie
    for i in range(len(text)):
        j = len(text)-i
        s_text = text[j:]
        pNode = root
       
        for k in range(len(s_text)):
            p = s_text[k]
            if p in pNode.children:
                pNode = pNode.children[p]
            else:
                idx = j if k == len(s_text)-1 else None
                childNode = Node(idx,pNode,p)
                pNode.children[p] = childNode
                pNode = childNode
    return root
    
def compressSuffixTrie(root):
    toprocess = [root]
    all_nodes = []
    while len(toprocess) >0:
        for tp in toprocess:
            all_nodes.append(tp)
            children = tp.children.values()
            toprocess.remove(tp)
            toprocess += children
    #compress
    for n in all_nodes:
        ch = n.children
        if len(ch) == 1:
            chi = list(n.children.values())[0]
            chich = chi.children
            
            n.nid = chi.nid
            
            del n.parent.children[n.label]
            n.label = n.label+chi.label
            n.parent.children[n.label] = n
            
            n.children = chich
            for chichi in chich.values():
                chichi.parent = n
            all_nodes.remove(chi)
    
    return root,all_nodes


def strSoFar(node):
    s = ""
    while node and node.label:
        s = node.label+s
        node = node.parent
    return s
def longestRepeat(text):#not working
    suffixTrie,allNodes = compressSuffixTrie(SuffixTrie(text+"$"))
    
    leafs = [l for l in allNodes if len(l.children) == 0 ]
    branches = {l.parent for l in leafs}
    
    bs = [strSoFar(b) for b in branches if len(b.children)>1]

    lrp = max(bs,key = lambda n:len(n))
    return lrp


f = open('C:/Users/grmsjac6/Downloads/dataset_296_5.txt')
toks = list(f)
text = toks[0].strip()
lrp = longestRepeat(text)
print lrp
               
    
    
                
        
                    
        
        
    
    
           
            
    
        
                
    