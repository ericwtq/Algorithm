import numpy as np


def find_minpath(adjacency):
    n = adjacency.length()
    mark_v = [[1]*n for q in range(n)]
    path = [[-1]*n for q in range(n)]
    for i in range(0,n):
        rk = 0
        mark_v[i][i] = -1
        while rk < n-1:
            temp_min = float("inf")
            for j in range(0,n):
                d_ij = adjacency.movetoindex(i).getData().movetoindex(j).getData()
                if temp_min > d_ij and mark_v[i][j] > 0:
                    temp_min = d_ij
                    vnear = j

            for k in range(0,n):
                d_ik = adjacency.movetoindex(i).getData().movetoindex(k).getData()
                d_ivnear = adjacency.movetoindex(i).getData().movetoindex(vnear).getData()
                d_vneark = adjacency.movetoindex(vnear).getData().movetoindex(k).getData()
                if d_ivnear + d_vneark < d_ik:
                    path[i][k] = vnear
                    adjacency.movetoindex(i).getData().movetoindex(k).setData(d_ivnear + d_vneark)

            mark_v[i][vnear] = -1
            rk += 1

    distance = [[0]*n for i in range(n)]
    for m in range(0,n):
        for q in range(0,n):
            distance[m][q] = adjacency.movetoindex(m).getData().movetoindex(q).getData()

    return np.matrix(distance), path