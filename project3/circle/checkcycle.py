def check_cylpre(adjlist, v, mark, parent):
    mark[v] = True
    for i in adjlist[v]:
        if mark[i] == False:
            if check_cylpre(adjlist,i,mark,v):
                return True
        elif parent != i:
            return True
    return False


def check_cyl(adjlist,n):
    mark = [False]*n
    for i in range(n):
        if mark[i] == False:
            if check_cylpre(adjlist, i, mark, -1):
                print("has circle")
                return
    print("do not have circle")

