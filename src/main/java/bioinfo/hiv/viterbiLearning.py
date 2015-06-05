'''
Created on Jun 5, 2015

@author: grmsjac6
'''

from markov import optimalPath
from parameterEstimation import parameterEstimation
from bioinfo.hiv.parameterEstimation import printMatrices

def viterbiLearning(iterations,x,alphabet,symbols,transition_mat,emission_mat):
    for iter in range(iterations):
        transitions = {(symbols[i],symbols[j]):transition_mat[i][j] for i in range(len(symbols)) for j in range(len(symbols)) }
        emissions = {(symbols[i],alphabet[j]):emission_mat[i][j] for i in range(len(symbols)) for j in range(len(alphabet)) }
        
        path = optimalPath(x, transitions, emissions, alphabet, symbols)
        
        transition_mat,emission_mat = parameterEstimation(x, alphabet, path, symbols)
    return transition_mat,emission_mat


def parseLines(lines):
    iterations = int(lines[0].strip())
    x = lines[2].strip()
    alphabet = lines[4].strip().split()
    symbols = lines[6].strip().split()
    tramat_lines = lines[9:9+len(symbols)]
    emismat_lines = lines[11+len(symbols):]
    
    tramat = [[float(l) for l in li.split()[1:]] for li in tramat_lines]
    emismat = [[float(l) for l in li.split()[1:]] for li in emismat_lines]
    
    return (iterations,x,alphabet,symbols,tramat,emismat)
def test_viterbiLearning():
    lines = [
             "100",
            "--------",
            "zyzxzxxxzz",
            "--------",
            "x y z",
            "--------",
            "A B",
            "--------",
            "    A    B",
            "A    0.599    0.401    ",
            "B    0.294    0.706    ",
            "--------",
            "    x    y    z",
            "A    0.424    0.367    0.209    ",
            "B    0.262    0.449    0.289"
        ]
    
    (iterations,x,alphabet,symbols,tramat,emismat) = parseLines(lines)
    tramat,emismat =  viterbiLearning(iterations,x,alphabet,symbols,tramat,emismat)
    
    printMatrices(tramat, emismat, symbols, alphabet)

def exam_viterbiLearning():
    lines = list(open('dataset_11632_10.txt'))
    
    (iterations,x,alphabet,symbols,tramat,emismat) = parseLines(lines)
    tramat,emismat =  viterbiLearning(iterations,x,alphabet,symbols,tramat,emismat)
    
    printMatrices(tramat, emismat, symbols, alphabet)
    
if __name__ == '__main__':
    exam_viterbiLearning()