import math
import numpy as np


def find_minpath(adjacency):
    n1 = len(adjacency)
    n = int((-1 + math.sqrt(1 + 8 * n1)) / 2)
    mark_v = [[1] * n for q in range(n)]
    path = [[-1]*n for q in range(n)]
    for i in range(0,n):
        rk = 0
        mark_v[i][i] = -1
        while rk < n-1:
            temp_min = float("inf")
            for j in range(0,n):
                d_ij = adjacency[int((max(i,j) + 1) * max(i,j) / 2 + min(i,j))]
                if temp_min > d_ij and mark_v[i][j] > 0:
                    temp_min = d_ij
                    vnear = j

            for k in range(0,n):
                d_ivnear = adjacency[int((max(i,vnear) + 1) * max(i,vnear) / 2 + min(i,vnear))]
                d_vneark = adjacency[int((max(k,vnear) + 1) * max(k,vnear) / 2 + min(k,vnear))]
                d_ik = adjacency[int((max(k,i) + 1) * max(k,i) / 2 + min(k,i))]
                if d_ivnear + d_vneark < d_ik:
                    path[i][k] = vnear
                    path[k][i] = vnear
                    adjacency[int((max(i,k) + 1) * max(i,k) / 2 + min(i,k))] = d_ivnear + d_vneark

            mark_v[i][vnear] = -1
            rk += 1

    distance = [[0]*n for i in range(n)]
    for m in range(0,n):
        for q in range(0,n):
            m_max_q = max(m, q)
            m_min_q = min(m, q)
            distance[m][q] = adjacency[m_min_q + (1 + m_max_q) * m_max_q // 2]

    return distance, path