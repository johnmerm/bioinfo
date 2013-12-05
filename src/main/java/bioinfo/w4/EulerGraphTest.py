'''
Created on Dec 5, 2013

@author: grmsjac6
'''
import unittest
from bioinfo.w4.EulerGraph import parseGraph,cycle


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
        
        assert sum([len(a) for a in graph.values()]) == 0 and sum([len(a) for a in rev_graph.values()])
        pass

    def testGraphWithData(self):
        file = open('C:/Users/grmsjac6.GLOBAL-AD/Downloads/dataset_57_2(2).txt')
        data = list(file)
        file.close()
        lines = data
        graph,rev_graph = parseGraph(lines)
        euCycle = cycle(graph,rev_graph)
        assert sum([len(a) for a in graph.values()]) == 0 and sum([len(a) for a in rev_graph.values()])
        print("->".join(cycle(graph,rev_graph)))

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testEulerCycle']
    unittest.main()