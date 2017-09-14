def bre_bippre(adjlist, v, mark, forv, k):
    mark[v] = k
    forv.append(v)
    while forv:
        j = forv[0]
        forv.pop(0)
        for i in adjlist[j]:
            if mark[i] == 0 :
                mark[i] = -mark[j]
                forv.append(i)
            if mark[i] == mark[j]:
                return False
    return True


def bre_bip(adjlist,n):
    mark = [0]*n
    forv = list()
    for i in range(n):
        if mark[i] == 0:
            if bre_bippre(adjlist, i, mark, forv, 1) == False:
                print("is not bipartite")
                return
    print("is bipartite")

