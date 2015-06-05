'''
Created on May 31, 2015

@author: giannis
'''


def allowedTrans(state,cnts,repeat=True):
    cnt = 0
    states = []
    if (len(state)>1):
        cnt = int(state[1:])
    if state == 'S':
        states =  ['I0','M1','D1']
    elif state.startswith('I'):
        states= ['I'+str(cnt)] if repeat else []
        if cnt<cnts:
            states += ['M'+str(cnt+1),'D'+str(cnt+1)]
    elif (state.startswith('M') or state.startswith('D')):
        states= ['I'+str(cnt)]
        if cnt<cnts:
            states += ['M'+str(cnt+1),'D'+str(cnt+1)]
    if states and cnt == cnts:
        states.append('E')
    return states

def testAllowedTrans(states = ['S'],visited=set()):
    for state in states:
        if state != 'E' and state not in visited:
            new_states = allowedTrans(state, 2)
            visited.add(state)
            print state+"->"+" ".join(new_states)
            testAllowedTrans(new_states,visited)

def normalize(mat):
    for (s,d) in mat.items():
        denom = sum(d.values())
        for (dk,dv) in d.items():
            d[dk] = float(dv)/denom 
    return mat
    
def hiddenMarkov(threshold,alphabet,alignments,pseudocount = 0):
    m = len(alignments[0])
    acc_al = [ sum([1. if a[i]=='-' else 0. for a in alignments])/len(alignments) < threshold for i in range(m)]
    
    states = [[] for i in range(len(alignments))]
    
    symb_emis = {}
    for i in range(len(alignments)):
        al = alignments[i]
        states[i] = ['S']
        cnt = 0
        for j in range(len(al)):
            c = al[j]
            if acc_al[j]:
                cnt = cnt+1
                if c == '-':
                    states[i].append('D'+str(cnt))
                else:
                    states[i].append('M'+str(cnt))
                    
                    if 'M'+str(cnt) not in  symb_emis:
                        symb_emis['M'+str(cnt)] = {}
                    if c not in symb_emis['M'+str(cnt)]:
                        symb_emis['M'+str(cnt)][c] = 1 
                    else:
                        symb_emis['M'+str(cnt)][c] += 1
                
            else:
                if c != '-':
                    states[i].append('I'+str(cnt))
                    if 'I'+str(cnt) not in  symb_emis:
                        symb_emis['I'+str(cnt)] = {}
                    if c not in symb_emis['I'+str(cnt)]:
                        symb_emis['I'+str(cnt)][c] = 1
                    else:
                        symb_emis['I'+str(cnt)][c] += 1
                    
        states[i].append('E')
    
    trans = {}
    

    for state in states:
        for i in range(len(state)-1):
            fro,to = state[i],state[i+1]
            
                
            if not fro in trans:
                trans[fro] = {}
            if not to in trans[fro]:
                trans[fro][to] = 0   
            trans[fro][to] +=1
            
    trans = normalize(trans)
        
    symb_emis = normalize(symb_emis)
            
    cnt = sum([1 if acc else 0 for acc in acc_al])
    all_states = ['S','I0']
    for i in range(cnt):
        all_states.append('M'+str(i+1))
        all_states.append('D'+str(i+1))
        all_states.append('I'+str(i+1))
    all_states.append('E')
    
    if pseudocount > 0:
        for state in all_states:
            if state !='E':
                trans[state] = {state_to:pseudocount + (trans[state][state_to] if state in trans and state_to in trans[state] else 0) for state_to in allowedTrans(state, cnt)}
                
            if state.startswith('I') or state.startswith('M'):
                symb_emis[state] = {state_to:pseudocount + (symb_emis[state][state_to] if state in symb_emis and state_to in symb_emis[state] else 0) for state_to in alphabet}
        
        trans = normalize(trans)
        symb_emis = normalize(symb_emis)
    
    trans_mat = [[trans[s1][s2] if s1 in trans and s2 in trans[s1] else 0 for s2 in all_states ]for s1 in all_states]
    ems_mat = [[symb_emis[st][sy] if st in symb_emis and sy in symb_emis[st] else 0 for sy in alphabet] for st in all_states]
    
    
    return all_states,trans_mat,ems_mat,trans,symb_emis,cnt
def test_hiddenMarkov():
    threshold = 0.289
    alphabet = ['A','B','C','D','E']
    alignments = [  'EBA',
                    'E-D',
                    'EB-',
                    'EED',
                    'EBD',
                    'EBE',
                    'E-D',
                    'E-D']
    
    return hiddenMarkov(threshold, alphabet, alignments)

def parse(lines):
    tp = [float(l) for l in lines[0].strip().split()]
    threshold = tp[0]
    pseudocount = tp[1] if len(tp)>1 else 0
    alphabet = lines[2].strip().split()
    alignments = [l.strip() for l in lines[4:]]
    return threshold,alphabet,alignments,pseudocount
def testParse():
    lines = ["0.252",
"--------",
"A B C D E",
"--------",
"DCDABACED",
"DCCA--CA-",
"DCDAB-CA-",
"BCDA---A-",
"BC-ABE-AE"]
    threshold,alphabet,alignments = parse(lines)
    pass

def exam_hiddenMarkov():
#     lines = [   "0.252",
#                 "--------",
#                 "A B C D E",
#                 "--------",
#                 "DCDABACED",
#                 "DCCA--CA-",
#                 "DCDAB-CA-",
#                 "BCDA---A-",
#                 "BC-ABE-AE"]
    lines = list(open('/home/giannis/Downloads/dataset_11632_2.txt'))
    threshold,alphabet,alignments = parse(lines)
    all_states,trans_mat,ems_mat  = hiddenMarkov(threshold,alphabet,alignments)
    print ' \t'+'\t'.join(all_states)
    for i in range(len(all_states)):
        print all_states[i]+'\t'+'\t'.join([str(t) for t in 
                                       trans_mat[i]])
    print "--------"
    
    print ' \t'+'\t'.join(alphabet)
    for i in range(len(all_states)):
        print all_states[i]+'\t'+'\t'.join([str(t) for t in 
                                      ems_mat[i]])


def test_PseudoCount():
    lines =["0.358 0.01",
            "--------",
            "A B C D E",
            "--------",
            "A-A",
            "ADA",
            "ACA",
            "A-C",
            "-EA",
            "D-A"]
    threshold,alphabet,alignments,pseudocount = parse(lines)
    all_states,trans_mat,ems_mat  = hiddenMarkov(threshold,alphabet,alignments,pseudocount)
    print ' \t'+'\t'.join(all_states)
    for i in range(len(all_states)):
        print all_states[i]+'\t'+'\t'.join([ "{0:.3f}".format(t) for t in 
                                       trans_mat[i]])
    print "--------"
    
    print ' \t'+'\t'.join(alphabet)
    for i in range(len(all_states)):
        print all_states[i]+'\t'+'\t'.join(["{0:.3f}".format(t) for t in 
                                      ems_mat[i]]) 



def exam_pseudoCount():
#     lines = [   "0.252",
#                 "--------",
#                 "A B C D E",
#                 "--------",
#                 "DCDABACED",
#                 "DCCA--CA-",
#                 "DCDAB-CA-",
#                 "BCDA---A-",
#                 "BC-ABE-AE"]
    lines = list(open('/home/giannis/Downloads/dataset_11632_4.txt'))
    threshold,alphabet,alignments,pseudocount = parse(lines)
    all_states,trans_mat,ems_mat  = hiddenMarkov(threshold,alphabet,alignments,pseudocount)
    print ' \t'+'\t'.join(all_states)
    for i in range(len(all_states)):
        print all_states[i]+'\t'+'\t'.join(["{0:.3f}".format(t) for t in 
                                       trans_mat[i]])
    print "--------"
    
    print ' \t'+'\t'.join(alphabet)
    for i in range(len(all_states)):
        print all_states[i]+'\t'+'\t'.join(["{0:.3f}".format(t) for t in 
                                      ems_mat[i]])




if __name__ == '__main__':
    exam_pseudoCount()