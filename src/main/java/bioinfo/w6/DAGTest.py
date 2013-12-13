'''
Created on Dec 13, 2013

@author: grmsjac6
'''
import unittest
from LCS import dag

class Test(unittest.TestCase):


    def testDAG(self):
        source = '0'
        sink = '4'
        lines=["0->1:7",
                "0->2:4",
                "2->3:2",
                "1->4:1",
                "3->4:3"]
        
        graph={}
        for line in lines:
            toks = line.split("->")
            key = toks[0]
            value = toks[1].split(":")
            vv = (value[0],int(value[1])) 
            if key in graph:
                graph[key].append(vv)
            else:
                graph[key]=[vv]
            
        dag(source, sink, graph)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testDAG']
    unittest.main()