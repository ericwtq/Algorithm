def tsp_heuristic(Adjmatrix,Adjlist,v):
    n = len(Adjmatrix)
    mark = [0]*n
    path = []
    mark[v] = 1
    path.append(v)
    while n - 1:
        dis_v = float("inf")
        new_v = Adjlist[v][0]
        for i in Adjlist[v]:
            if Adjmatrix[v][i] < dis_v and mark[i] != 1:
                dis_v = Adjmatrix[v][i]
                new_v = i
        v = new_v
        mark[v] = 1
        path.append(v)
        n -= 1
    return path