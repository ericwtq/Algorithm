import numpy as np
def find_minpath(adjacency):
    distance = adjacency
    n = len(distance)
    path = [[-1]*n for i in range(0,n)]
    for k in range(0, n):
        for i in range(0, n):
            for j in range(0, n):
                if (distance[i][k] + distance[k][j]) < distance[i][j]:
                    distance[i][j] = distance[i][k] + distance[k][j]
                    path[i][j] = k
    return distance, path


