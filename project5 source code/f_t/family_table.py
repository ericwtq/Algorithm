def augmenting_path(s,t,C,parent,n):
    mark = [0]*n
    mark[s] = 1
    v_bfs = []
    v_bfs.append(s)
    while v_bfs:
        curr = v_bfs.pop(0)
        #for i in Adj[curr]:
        for i, val in enumerate(C[curr]):
            if mark[i] != 1 and val > 0:
                mark[i] = 1
                v_bfs.append(i)
                parent[i] = curr
    return True if mark[t] else False


def max_flow_2F(s,t,C,n):
    parent = [-1]*n
    maxflow = 0
    while augmenting_path(s,t,C,parent,n):
        f_ij = float("inf")
        curr1 = t
        while curr1 != s:
            f_ij = min(f_ij,C[parent[curr1]][curr1])
            curr1 = parent[curr1]
        maxflow += f_ij
        curr2 = t
        while curr2 != s:
            C[parent[curr2]][curr2] -= f_ij
            C[curr2][parent[curr2]] += f_ij
            curr2 = parent[curr2]
    return C, maxflow
