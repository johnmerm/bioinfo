'''
Created on Jun 11, 2015

@author: grmsjac6
'''
import unittest


masses = {li.strip().split()[0]:int(li.strip().split()[1]) for li in list(open('integer_mass_table.txt')) } 

def multi_dict(dict,kv):
    (k,v) = kv
    if v in dict:
        dict[v].append(k)
    else:
        dict[v] = [k]
    return dict

masses_rev = reduce(multi_dict, masses.items(),{})



def spectrumGraph(spectrum):
    if spectrum[0] != 0:
        spectrum = [0]+spectrum
    diffs = {(spectrum[i],spectrum[j]):masses_rev[spectrum[j]-spectrum[i]][0] for i in range(len(spectrum)) for j in range(len(spectrum)) if spectrum[j]-spectrum[i] in masses_rev}
    return '\n'.join([':'.join(['->'.join([str(k[0]),str(k[1])]),v]) for k,v in sorted(diffs.items())]),diffs

def spectrumPath(spectrum,half=False):
    out,sg = spectrumGraph(spectrum)
    sgb = {}
    for ((f,t),v) in sg.items():
        if f in sgb:
            sgb[f].append((t,v))
        else:
            sgb[f] = [(t,v)]
    
    paths = []
    def follow(path):
        
        if path[-1] in sgb:
            nx = sgb[path[-1]]
            for n in nx:
                follow(path+[n[0]])
        else:
            if path[-1] == spectrum[-1]:
                spec = [path[i]- path[0] for i in range(1,len(path))]
                if half:
                    a_spec = spec
                else:
                    reverse_spec = [path[-1]- path[i] for i in range(1,len(path))]
                    
                    a_spec = sorted(spec+reverse_spec)[1:]
                if a_spec == spectrum:
                    ps = [sg[(path[i],path[i+1])] for i in range(len(path)-1)]
                    paths.append(''.join(ps))
    
    follow([0])
    path = paths[0]
    
    return path


def spectrumVector(p_string,_masses = masses):
    p_mass = [_masses[p] for p in p_string]
    p_sums = [sum(p_mass[:i]) for i in range(len(p_mass)+1)]
    p_vector = [1 if i in p_sums else 0 for i in range(1,p_sums[-1]+1)]
    return p_vector

def inverseSpectrumVector(vector):
    
    spectrum = [i+1 for i in range(len(vector)) if vector[i]==1]
    return spectrumPath(spectrum,True)


def testVector():
        p_string = 'XZZXX'
        vector = spectrumVector(p_string)
        v_string = ' '.join([str(v) for v in vector])
        print v_string
        print '0 0 0 1 0 0 0 0 1 0 0 0 0 1 0 0 0 1 0 0 0 1'
        assert v_string == '0 0 0 1 0 0 0 0 1 0 0 0 0 1 0 0 0 1 0 0 0 1'

def testInverseVector():
    v_string = '0 0 0 1 0 0 0 0 1 0 0 0 0 1 0 0 0 1 0 0 0 1'
    v_l = v_string.split()
    vector = [int(v) for v in v_l]
    path = inverseSpectrumVector(vector)
    print path
    assert path == 'XZZXX'
def exam_vectorPath():
    line = list(open('dataset_11813_6.txt'))[0].strip()
    vector = spectrumVector(line)
    s=  ' '.join([str(v) for v in vector])
    f=  open('out.txt','w')
    f.write(s)
    f.close()
def exam_inverseVector():
    line = list(open('dataset_11813_8.txt'))[0].strip()
    vector = [int(v) for v in line.split()]
    path = inverseSpectrumVector(vector)
    print path
    
    
    
def exam_spectrumGraph():
    line = list(open('dataset_11813_2.txt'))[0].strip()
    spectrum = [int(l) for l in line.split()]
    out,sg = spectrumGraph(spectrum) 
    print out


def exam_spectrumPath():
    line = list(open('dataset_11813_4.txt'))[0].strip()
    spectrum = [int(l) for l in line.split()]
    path = spectrumPath(spectrum) 
    print path
class Test(unittest.TestCase):


    def setUp(self):
        pass


    def tearDown(self):
        pass


    def testSpectrumGraph(self):
        line = '57 71 154 185 301 332 415 429 486'
        out = '\n'.join(['0->57:G',
                '0->71:A',
                '57->154:P',
                '57->185:K',
                '71->185:N',
                '154->301:F',
                '185->332:F',
                '301->415:N',
                '301->429:K',
                '332->429:P',
                '415->486:A',
                '429->486:G'])
        
        spectrum = [int(l) for l in line.split()]
        diffs,sg = spectrumGraph(spectrum)
        assert diffs == out 
    
    def testSpectrumPath(self):
        line = '57 71 154 185 301 332 415 429 486' 
        spectrum = [int(l) for l in line.split()]
        path = spectrumPath(spectrum)
        assert path == 'GPFNA'
        
    
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    #unittest.main()
    exam_inverseVector()
    