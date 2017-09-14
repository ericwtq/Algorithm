import numpy as np
import random

def not_empty(s):
    return s and s.strip()

class graph():
    def __init__(self):
        self.num_vertice = 0
        self.solution = 0
        self.solution_best = 0
        self.num_sol = 0
        self.num_sol_best = 0
        self.adjmatrix = 0


def get_graph(filename):
    A = graph()
    lines = open(filename, 'r').readlines()
    adjancy = [line.strip().split(' ') for line in lines ]

    for i in range(0,len(adjancy)):
        adjancy[i] = list(filter(not_empty,adjancy[i]))
        adjancy[i] = [0 if x == '.' else 1 for x in adjancy[i]]

    A.adjmatrix = adjancy
    A.num_vertice = len(adjancy)
    A.solution = [0]*len(adjancy)
    A.solution_best = [0]*len(adjancy)
    return A





def sparse_array(n):
    topv = []
    sarray =[float("inf")]*((1 + n) * n // 2)
    allv = [i for i in range((1 + n) * n // 2)]
    for i in range(0, n):
        sarray[i + (i + 1) * i // 2] = 0
        topv.append(i + (i + 1) * i // 2)
    for j in topv:
        allv.remove(j)
    r = random.sample(allv,n-1)
    for k in r:
        sarray[k] = np.random.randint(1,n)
    return sarray


def sparse_matrix(n):
    A=graph()
    sarray = sparse_array(n)
    smatrix = [[0 for col in range(n)] for row in range(n)]

    for i in range(0, n):
        for j in range(0, n):
            i_max_j = max(i, j)
            i_min_j = min(i, j)
            smatrix[i][j] = sarray[i_min_j + (1 + i_max_j) * i_max_j // 2]

    for i in range(0,len(smatrix)):
        smatrix[i] = [0 if x == float("inf") else 1 for x in smatrix[i]]
        smatrix[i][i] = 0

    A.adjmatrix = smatrix
    A.num_vertice = len(smatrix)
    A.solution = [0] * len(smatrix)
    A.solution_best = [0] * len(smatrix)

    return A