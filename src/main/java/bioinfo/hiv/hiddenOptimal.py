'''
Created on Jun 1, 2015

@author: giannis
'''
import hiddenProfile as hp 
import markov as mp

def letter_func(path,x):
    if path[-1].startswith('D') or path[-1].startswith('E'):
        return '-'
    else:
        cnts = len([p for p in path if p.startswith('M') or p.startswith('I')])
        if cnts>len(x):
            return None
        else:
            return x[cnts-1]



        
            
    
def optimalHidden(x, threshold, alphabet, alignments, pseudocount):
    all_states,trans_mat,ems_mat,trans,symb_emis,cnts= hp.hiddenMarkov(threshold, alphabet, alignments, pseudocount)
    
    def weight(sf,cf,st,ct,p):
        
        symbol = x[p-1] if p>0 else ''
        _from = sf+ (str(cf) if cf !=None else '')
        _to = st+ str(ct)
        
        prod = trans[_from][_to] if _from in trans and _to in trans[_from] else 0
        if st != 'D':
            prod *=  symb_emis[_to][symbol] if _to in symb_emis and symbol in symb_emis[_to] else 0
        return prod
        
    scores = {}
    
    
    
    def allowed_states(s,c,p):
        return  (s=='S'and c == None and p==0) or (s == 'D' and c>0 and p>=0 ) or (s=='M' and c>0 and p>0) or (s=='I' and c>=0 and p>0)
     
    def come_from(s,c,p):
        if s == 'E': 
            return {('M',cnts,len(x)),('D',cnts,len(x)),('I',cnts,len(x))}
        
        ret = set({})
        
        if (s,c,p) == ('I',0,1) or (s,c,p)==('M',1,1) or (s,c,p) ==('D',1,0):
            ret = {('S',None,0)}
        else:
            if s == 'M':
                ret = ret.union({('M',c-1,p-1),('D',c-1,p-1),('I',c-1,p-1)})
            elif s == 'D':
                ret = ret.union({('M',c-1,p),('D',c-1,p),('I',c-1,p)})
            elif s == 'I':
                ret = ret.union({('M',c,p-1),('D',c,p-1),('I',c,p-1)})
        
        return {(_s,_c,_p) for (_s,_c,_p) in ret  if allowed_states(_s,_c,_p)}
        
    def score(s,c,p):
        if (s,c,p) in scores:
            return scores[s,c,p]
        else:
            #print (s,c,p)  
            sc = 0
            if s == 'S':
                sc = 1
            else:
                
                cmf = come_from(s, c, p)
                scs = {(sf,cf,pf):score(sf,cf,pf)*weight(sf,cf,s,c,p) for (sf,cf,pf) in  cmf}
                sc= max(scs.items(),key = lambda x:x[1])
                sc = sc[1]
            scores[(s,c,p)] = sc
            #print (s,c,p ,sc)
            return sc
        return None
    
    for i in range(1,cnts+1):
        for j in range(1,len(x)+1):
            for s in ['D','I','M']:
                score(s,i,j)
    
    ret = ['E']
    cfm = (('E',None,None),None)
    while cfm[0][0]!='S':
        cf_1,cf_2,cf_3 = cfm[0]                
        cfe = come_from(cf_1,cf_2,cf_3)
        cfs = {(es,sc,ep):scores[es,sc,ep] for (es,sc,ep) in cfe if (es,sc,ep) in scores}
        cfm = max(cfs.items(),key=lambda x:x[1]) 
        ret = [ cfm[0][0]+  ( str(cfm[0][1]) if cfm[0][1] !=None else '')] + ret
    return ret
def test_optimalHidden():
    lines=["AEFDFDC",
            "--------",
            "0.4 0.01",
            "--------",
            "A B C D E F",
            "--------",
            "ACDEFACADF",
            "AFDA---CCF",
            "A--EFD-FDC",
            "ACAEF--A-C",
            "ADDEFAAADF"
            ]
    x = lines[0].strip()
    threshold,alphabet,alignments,pseudocount = hp.parse(lines[2:])
    hi =  optimalHidden(x, threshold, alphabet, alignments, pseudocount)
    
    #M1 D2 D3 M4 M5 I5 M6 M7 M8
    print ' '.join(hi) 
    return hi


def exam_optimalHidden():
    lines = list(open('dataset_11632_6.txt'))
    x = lines[0].strip()
    threshold,alphabet,alignments,pseudocount = hp.parse(lines[2:])
    hi =  optimalHidden(x, threshold, alphabet, alignments, pseudocount)
    
    #M1 D2 D3 M4 M5 I5 M6 M7 M8
    print ' '.join(hi) 
    return hi
    
if __name__ == '__main__':
    exam_optimalHidden()