import math
import numpy as np

def find_minpath(adjacency):
    n1 = len(adjacency)
    n = int((-1 + math.sqrt(1 + 8 * n1)) / 2)
    path = [[-1]*n for i in range(n)]
    for k in range(0, n):
        for i in range(0, n):
            for j in range(0, n):
                d_ik = adjacency[int((max(i,k) + 1) * max(i,k) / 2 + min(i,k))]
                d_kj = adjacency[int((max(k,j) + 1) * max(k,j) / 2 + min(k,j))]
                d_ij = adjacency[int((max(i,j) + 1) * max(i,j) / 2 + min(i,j))]
                if d_ik + d_kj < d_ij:
                    adjacency[int((max(i, j) + 1) * max(i, j) / 2 + min(i, j))] = d_ik +d_kj
                    path[i][j] = k


    distance = [[0]*n for i in range(n)]
    for m in range(0,n):
        for q in range(0,n):
            m_max_q = max(m, q)
            m_min_q = min(m, q)
            distance[m][q] = adjacency[int(m_min_q + (1 + m_max_q) * m_max_q / 2)]


    return np.matrix(distance), path
