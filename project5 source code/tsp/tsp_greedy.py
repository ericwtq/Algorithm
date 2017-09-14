def root(parent,v):
    if parent[v] == v:
        return v
    return root(parent,parent[v])

def connect(order,parent,v1,v2):
    root1 = root(parent,v1)
    root2 = root(parent,v2)
    if order[root1] == order[root2]:
        parent[root2] = root1
        order[root1] += 1
    elif order[root1] > order[root2]:
        parent[root2] = root1
    else:
        parent[root1] = root2

def tsp_greedy(s_graph,n):
    path =[]
    mark = [0]*n
    order = [0]*n
    parent = []
    k = 0
    for i in range(n):
        parent.append(i)
    while n - 1 > 0:
        v1 = s_graph[k][0]
        v2 = s_graph[k][1]
        i = root(parent,v1)
        j = root(parent,v2)
        if i != j and mark[v1] < 2 and mark[v2] < 2:
            n -= 1
            path.append(s_graph[k])
            mark[v1] += 1
            mark[v2] += 1
            connect(order,parent,v1,v2)
        k += 1
    return path,mark