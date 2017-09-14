from collections import defaultdict

def not_empty(s):
    return s and s.strip()
def get_matrix(filename):
    lines = open(filename, 'r').readlines()
    distance_mat = [line.strip().split(' ') for line in lines ]
    for i in range(0,len(distance_mat)):
        distance_mat[i] = list(filter(not_empty,distance_mat[i]))
        distance_mat[i] = [float('inf') if x == '.' else x for x in distance_mat[i]]
        distance_mat[i] = [int(x) if x != float('inf') else x for x in distance_mat[i]]
        distance_mat[i][i] = 0
    return distance_mat

def get_adjlist(filename):
    D = get_matrix(filename)
    adjlist = defaultdict(list)
    N = len(D)
    for m in range(N):
        for n in range(N):
            if D[m][n] != 0:
                adjlist[m].append(n)
    return adjlist


def edge_G(filename):
    D = get_matrix(filename)
    E_G=[]
    N = len(D)
    for i in range(N):
        for j in range(N):
            if i < j and D[i][j] != 0 and D[i][j] != float("inf"):
                edge = [i,j,D[i][j]]
                E_G.append(edge)
    E_graph = sorted(E_G, key=lambda x: x[2])
    return E_graph

