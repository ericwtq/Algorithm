


def find_minpath(adjacency):
    n = len(adjacency)
    mark_v = [[1]*n for q in range(n)]
    path = [[q]*n for q in range(n)]
    for i in range(0,n):
        rk = 0
        mark_v[i][i] = -1
        while rk < n-1:
            temp_min = float("inf")
            for j in range(0,n):
                if temp_min > adjacency[i][j] and mark_v[i][j] > 0:
                    temp_min = adjacency[i][j]
                    vnear = j

            for k in range(0,n):
                if adjacency[i][vnear] + adjacency[vnear][k] < adjacency[i][k]:
                    path[i][k] = vnear
                    adjacency[i][k] = adjacency[i][vnear] + adjacency[vnear][k]

            mark_v[i][vnear] = -1
            rk += 1
    return adjacency, path
