import numpy as np


def find_minpath(adjacency):
    n = adjacency.length()
    path = [[-1]*n for i in range(0,n)]
    for k in range(0,n):
        for i in range(0,n):
            for j in range(0,n):
                d_ij = adjacency.movetoindex(i).getData().movetoindex(j).getData()
                d_ik = adjacency.movetoindex(i).getData().movetoindex(k).getData()
                d_jk = adjacency.movetoindex(j).getData().movetoindex(k).getData()
                if d_ij > d_ik + d_jk:
                    path[i][j] = k
                    adjacency.movetoindex(i).getData().movetoindex(j).setData(d_ik + d_jk)

    distance = [[0]*n for i in range(n)]
    for m in range(0,n):
        for q in range(0,n):
            distance[m][q] = adjacency.movetoindex(m).getData().movetoindex(q).getData()

    return np.matrix(distance), path
