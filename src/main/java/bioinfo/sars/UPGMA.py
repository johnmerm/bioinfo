from timeit import itertools
import unittest



def UPGMA(Data,n):
    gen = n
    
    Clusters = {i:[i] for i in range(n)}
    all_Clusters = {i:[i] for i in range(n)}
    T = {i:[] for i in range(n)}
    
    distCache = {(i,j):Data[i][j] for i in range(n) for j in range(n)}
    
    Age = {i:0 for i in range(n)}
    
    def dist(clust1,clust2):
        if (clust1,clust2) in distCache:
            return distCache[(clust1,clust2)]
        else:
            dd = sum([ sum([ Data[i][j] for j in Clusters[clust2]]) for i in Clusters[clust1]])/(len(Clusters[clust1])*len(Clusters[clust2]))
            distCache[(clust1,clust2)] = dd
            distCache[(clust2,clust1)] = dd
            return dd 
    
    while len(Clusters)>1:
        permuts = itertools.permutations(Clusters.keys(),2)
        closest = min(permuts,key = lambda x:dist(x[0],x[1]))
        Clusters[gen] = Clusters[closest[0]]+Clusters[closest[1]]
        
        T[gen] = [closest[0],closest[1]]
        Age[gen] = dist(closest[0],closest[1])/2
        
        all_Clusters[gen] = Clusters[closest[0]]+Clusters[closest[1]]
        
        del Clusters[closest[0]]
        del Clusters[closest[1]]
        
        for c in Clusters:
            dist(gen,c)
        gen = gen+1
    
    
    TA = {}
    
    for (k,vv) in T.items():
        if len(vv)>0:
            TA[k] = {}
            for v in vv:
                TA[k][v] = Age[k]-Age[v]
    
    return TA
        
def exam_UPGMA():
    lines = list(open('dataset_10332_8.txt'))
    n = int(lines[0].strip())
    Data = [[float(d) for d in ld.strip().split()]for ld in lines[1:] ]
    TA = UPGMA(Data, n)
    for (k,vd) in TA.items():
        for (v,d) in vd.items():
            print str(k)+'->'+str(v)+':'+str(d)
            print str(v)+'->'+str(k)+':'+str(d)
                             
  
class Test(unittest.TestCase):
    def testUPGMA(self):
        lines = ['4','0    20    17    11','20    0    20    13','17    20    0    10','11    13    10    0']
        n = int(lines[0].strip())
        Data = [[float(d) for d in ld.strip().split()]for ld in lines[1:] ]
        

        TA = UPGMA(Data, n)
        for (k,vd) in TA.items():
            for (v,d) in vd.items():
                print str(k)+'->'+str(v)+':'+str(d)
                print str(v)+'->'+str(k)+':'+str(d)
        
        pass #Checked

if __name__ == '__main__':
     #import sys;sys.argv = ['', 'Test.testName']
    exam_UPGMA()