from numpy import Inf
alphabet = ['A','C','G','T']

def parseNodes(lines):
    edges = {}
    for line in lines:
        tokens = line.split('->')
        _from = tokens[0]
        _to = tokens[1]
        
        if _to not in edges:
            edges[_to] = []
        if _from in edges:
            edges[_from].append(_to)
        else:
            edges[_from] = [_to]

def isRipe(node,T,tags):
    return tags[node] == 0 and T[node]!=None and all([tags[c]==1 for c in T[node]])

def smallParsimony(T,Character):
    Tag = {}
    s={k:{} for k in alphabet}
    for node,children in T.items():
        if children == None:
            Tag[node] = 1
            for k in alphabet:
                s[k][node] = 0 if node[Character] == k else Inf
        else:
            Tag[node] = 0
    
    ripes = [n for n in T.keys() if isRipe(n,T,Tag)]
    while len(ripes)>0:
        ripe = ripes[0]
        Tag[ripe] = 1
        children = T[ripe]     
        for k in alphabet:
            childrenscore = [[s[i][c]+ (1 if k!=i else 0 )for i in alphabet] for c in children]
            childrenscore = [min(ch) for ch in childrenscore]
            childrenscore = sum(childrenscore)
            s[k][ripe] =  childrenscore
        ripes = [n for n in T.keys() if isRipe(n,T,Tag)]
    
    ret = {}
    for v in T.keys():
        
        ma = [(k,s[k][v]) for k in alphabet]
        ma = min(ma,key=lambda x:x[1])
        ret[v] = ma
    return ret


def dist(a,b):
    dif = [i for i in range(len(a)) if a[i]!=b[i]]
    return len(dif)
def test_smappParsimony():
    n = 4
    T = {'CAAATCCC':None,
         'ATTGCGAC':None,
         'CTGCGCTG':None,
         'ATGGACGA':None,
         4:['CAAATCCC','ATTGCGAC'],
         5:['CTGCGCTG','ATGGACGA'],
         6:[4,5]}
    
    branches = [v for v in T.keys() if T[v]!=None]
    
    sps = [ smallParsimony(T, c) for c in range(8)]
    
    spv = {v:''.join([sps[i][v][0] for i in range(len(sps))]) for v in branches }
    
    for v in branches:
        for c in T[v]:
            val = (spv[c] if c in spv else c)
            print spv[v]+'->'+val+':'+str(dist(spv[v],val))
            print val+'->'+spv[v]+':'+str(dist(spv[v],val))
            
    
if __name__ == '__main__':
    sp = test_smappParsimony()
    print sp