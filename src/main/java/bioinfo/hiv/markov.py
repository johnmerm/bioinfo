'''
Created on May 26, 2015

@author: grmsjac6
'''

def markov(path,symbols,transitions):
    p = 1.0/len(symbols)
    for i in range(len(path)-1):
        _this = path[i]
        _next = path[i+1]
        pTrans = transitions[(_this,_next)]
        p = p* pTrans;
    return p

def test_Markov():
    path = 'BAAAAAAAABBBBBABBBBABAAAAABBBBAABBAABABBBABBAABAAB'
    symbols = ['A','B']
    
       

    transitions = {
             ('A','A'):0.192     ,
             ('A','B'):0.808,
             ('B','A'):0.77   ,
             ('B','B'): 0.23}
    p = markov(path, symbols, transitions)
    return p;
    

def emission(x,path,transitions,alphabet=['x','y','z'],symbols=['A','B']):
    p = 1.0
    for i in range(len(path)):
        state = path[i]
        em = x[i]
        pTrans = transitions[(state,em)]
        p = p* pTrans;
    return p

def test_emission():
    x = 'yzyyzyyxyxxyzyxxzxyzzyxxxxxyxzxxyzzzxyyxyzxzxxyyyx'
    path = 'ABAAAAABAABAAABBBAABABBABABBBBBABABABAAABABAAABABB'
    
    alphabet=['x','y','z']
    symbols=['A','B']
    
    transitions_mat =[[ 0.487,    0.017,    0.496],[0.431,    0.379,    0.19]]
    transitions = {(symbols[i],alphabet[j]):transitions_mat[i][j] for i in range(len(symbols)) for j in range(len(alphabet)) }
    
    return emission(x, path, transitions, alphabet, symbols)

def prod(itera):
    return reduce(lambda x,y:x*y,itera,1)

def letter_simple(path,x):
    cnt = len(path)
    return x[cnt-1]

def optimalPath(x,transitions,emissions,alphabet=['x','y','z'],symbols=['A','B'],letter_func = letter_simple,init_states=None):
    if init_states == None:
        init_states = symbols
    scores = {s:{e:(ev/len(symbols),[s]) for (e,ev) in emissions.items() if e[0]==s and e[1]==letter_func([s],x)} for s in init_states}
    scores = {s:max(v.values(),key=lambda x:x[0]) for (s,v) in scores.items()}
    
    for i in range (1,len(x)):
    
        
        states = {t for t in symbols for s in scores.keys() if (s,t) in transitions} 
        
        new_scores = {s:{t[0]:((scores[t[0]][0],tv,ev),scores[t[0]][1]) for (t,tv) in transitions.items() for (e,ev) in emissions.items() 
                         if t[0] in scores and e[1] == letter_func(scores[t[0]][1]+[s],x) and t[1]==s and e[0] == s
                         } for s in states }
        
        new_scores = {s:{tk:(prod(tv[0]),tv[1]+[s]) for (tk,tv) in v.items()}  for (s,v) in new_scores.items()}
        
        new_scores = {s:max(v.values(),key=lambda x:x[0]) for (s,v) in new_scores.items() if len(v.values())>1}
        
        
        scores = new_scores
        cand = max(scores.values())[1]
    return max(scores.values())[1]


def viterbi(x,transitions,emissions,alphabet=['x','y','z'],symbols=['A','B'],func=sum):
    trail = []
    
    scores = {s:{e:ev/len(symbols) for (e,ev) in emissions.items() if e[0]==s and e[1]==x[0]} for s in symbols}
    scores = {s:func(v.values()) for (s,v) in scores.items()}
    trail.append(scores)
    
    for i in range (1,len(x)):
        em = x[i]
        new_scores = {s:{t[0]:(scores[t[0]],tv,ev) for (t,tv) in transitions.items() for (e,ev) in emissions.items() 
                         if e[1] == em and t[1]==s and e[0] == s
                         } for s in symbols }
        
        new_scores = {s:{tk:prod(tv) for (tk,tv) in v.items()}  for (s,v) in new_scores.items()}
        
        new_scores = {s:func(v.values()) for (s,v) in new_scores.items()}
        scores = new_scores
        trail.append(scores)
    
        
    return func(new_scores.values()),trail
def forward(x,transitions,emissions,alphabet=['x','y','z'],symbols=['A','B']):
    return viterbi(x, transitions, emissions, alphabet, symbols, sum)


    
def test_optimalPath():
    x='xyxzzxyxyy'
    alphabet=['x','y','z']
    symbols=['A','B']
    
    transition_mat=[[0.641,    0.359],
                    [0.729,    0.271]]
    
    emission_mat = [[0.117,    0.691,   0.192],
                    [0.097,    0.42,    0.483]]
    
    transitions = {(symbols[i],symbols[j]):transition_mat[i][j] for i in range(len(symbols)) for j in range(len(symbols)) }
    emissions = {(symbols[i],alphabet[j]):emission_mat[i][j] for i in range(len(symbols)) for j in range(len(alphabet)) }
    
    path = optimalPath(x, transitions, emissions, alphabet, symbols)
    print ''.join(path)
    

def exam_optimalPath():
    x,transitions,emissions,alphabet,symbols = parseFile('dataset_11594_6.txt')
    
    path = optimalPath(x, transitions, emissions, alphabet, symbols)
    print ''.join(path)

def test_forward():
    x='xzyyzzyzyy'
    alphabet=['x','y','z']
    symbols=['A','B']
    
    transition_mat=[[0.303,    0.697 ],
[    0.831,    0.169 ]]
    
    emission_mat = [[0.533,    0.065  ,  0.402 ],
[    0.342,    0.334,    0.324]]
    
    transitions = {(symbols[i],symbols[j]):transition_mat[i][j] for i in range(len(symbols)) for j in range(len(symbols)) }
    emissions = {(symbols[i],alphabet[j]):emission_mat[i][j] for i in range(len(symbols)) for j in range(len(alphabet)) }
    
    return forward(x, transitions, emissions, alphabet, symbols)

def exam_forward():
    
    x,transitions,emissions,alphabet,symbols = parseFile('C:/Users/grmsjac6/Downloads/dataset_11594_8.txt') 
    return forward(x, transitions, emissions, alphabet, symbols)

def parseFile(filename):
    al = list(open(filename))
    
    x= al[0].strip()
    
    alphabet=al[2].strip().split(' ')
    symbols=al[4].strip().split(' ')
    
    tran_lines = al[7:7+len(symbols)]
    emis_lines = al[9+len(symbols):10+len(symbols)+len(alphabet)]
    
    transition_mat = [[float(t) for t in ts.split()[1:]] for ts in tran_lines]
    emission_mat = [[float(t) for t in ts.split()[1:]] for ts in emis_lines]
        
    transitions = {(symbols[i],symbols[j]):transition_mat[i][j] for i in range(len(symbols)) for j in range(len(symbols)) }
    emissions = {(symbols[i],alphabet[j]):emission_mat[i][j] for i in range(len(symbols)) for j in range(len(alphabet)) }
    
    return x,transitions,emissions,alphabet,symbols
    
if __name__ == '__main__':
    result = test_optimalPath()
    
  
