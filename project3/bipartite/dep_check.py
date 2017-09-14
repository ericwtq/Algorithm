
def dep_bippre(adjlist1,mark,v,k):
    mark[v] = k
    for i in adjlist1[v]:
        if mark[i] == k:
            return False
        if mark[i] == 0:
            if dep_bippre(adjlist1,mark,i,-k) == False:
                return False
    return True


def dep_bip(adjlist1, n):
    mark = [0]*n
    for i in range(n):
        if mark[i] == 0:
            if dep_bippre(adjlist1,mark,i,1) == False:
                print("is not bipartite")
                return
    print("is bipartite")

