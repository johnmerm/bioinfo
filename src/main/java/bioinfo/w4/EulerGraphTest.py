'''
Created on Dec 5, 2013

@author: grmsjac6
'''
import unittest
from bioinfo.w4.EulerGraph import parseGraph,cycle,paths


class Test(unittest.TestCase):


    def testEulerCycle(self):
        lines =["0 -> 3",
                "1 -> 0",
                "2 -> 1,6",
                "3 -> 2",
                "4 -> 2",
                "5 -> 4",
                "6 -> 5,8",
                "7 -> 9",
                "8 -> 7",
                "9 -> 6"]
        graph,rev_graph = parseGraph(lines)
        euCycle = cycle(graph,rev_graph)
        sa = sum([len(a) for a in graph.values()])
        sb = sum([len(a) for a in rev_graph.values()])
        assert sa == sb == 0 
        

    def skiptestGraphWithData(self):
        file = open('C:/Users/grmsjac6.GLOBAL-AD/Downloads/dataset_57_2(2).txt')
        data = list(file)
        file.close()
        lines = data
        graph,rev_graph = parseGraph(lines)
        euCycle = cycle(graph,rev_graph)
         
        sa = sum([len(a) for a in graph.values()])
        sb = sum([len(a) for a in rev_graph.values()])
        assert sa == sb == 0,"->".join(cycle(graph,rev_graph)) 
         
        
        
    def testPath(self):
        lines = ["0 -> 2",
                 "1 -> 3",
                 "2 -> 1",
                 "3 -> 0,4",
                 "6 -> 3,7",
                 "7 -> 8",
                 "8 -> 9",
                 "9 -> 6"]
        file = open('/home/giannis/Downloads/dataset_57_5(1).txt')
        data = list(file)
        file.close()
        lines = data#[2:-2]
        
        graph,rev_graph = parseGraph(lines)
        pp = sorted(paths(graph, rev_graph),key= lambda x:len(x),reverse=True)
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testEulerCycle']
    unittest.main()