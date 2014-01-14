'''
Created on Jan 14, 2014

@author: giannis
'''

def SuffixArray(text):
    all_sufs = []
    for i in range(len(text)):
        all_sufs.append((i,text[i:]))
    
    all_sufs = sorted(all_sufs,key=lambda x:x[1])
    return [x[0] for x in all_sufs]


f=open('dataset_96_3.txt')
text = next(f).strip()
sar = SuffixArray(text)
print(sar)