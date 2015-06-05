def dist(c1,c2,D):
    sum(
        [sum(
             [D[i][j] for j in range(len(D[i]))]
             ) for i in range(len(D))]
        )

def UPGMA(D,n):
    clusters = [i for i in range(n)]
    T = {c:[] for c in clusters}
    age = {c:0 for c in clusters}
    while len(clusters)>1:
        
    


if __name__ == '__main__':
    pass