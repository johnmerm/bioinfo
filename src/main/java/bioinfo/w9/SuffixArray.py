'''
Created on Jan 14, 2014

@author: giannis
'''

def SuffixArray(text):
    all_sufs = list(range(len(text)))
    all_sufs = sorted(all_sufs,key=lambda x:text[x:])
    return all_sufs


