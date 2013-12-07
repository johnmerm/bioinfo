'''
Created on Dec 7, 2013

@author: giannis
'''
import unittest

from EulerGraph import parseGraph
from StringReconstruction import StringReconstruction
from bioinfo.w4.StringReconstruction import UniversalString

class Test(unittest.TestCase):


    def testStringReconstruction(self):
        lines=  ["CTT -> TTA",
                 "ACC -> CCA",
                 "TAC -> ACC",
                 "GGC -> GCT",
                 "GCT -> CTT",
                 "TTA -> TAC"]
        
#         file = open('/home/giannis/Downloads/dataset_57_6.txt')
#         data = list(file)
#         file.close()
#        lines = data
        
        graph,rev_graph = parseGraph(lines)
        string =  StringReconstruction(graph, rev_graph)
        assert string == 'GGCTTACCA'
    
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testStringReconstruction']
    unittest.main()