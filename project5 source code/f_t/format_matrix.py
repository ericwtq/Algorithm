from collections import defaultdict

def flow_m(table, family):
    ntable = len(table)
    nfamily = len(family)
    N = 2+ntable+nfamily
    C = [[0]*N for q in range(N)]
    for i in range(ntable):
        C[1 + nfamily + i][N - 1] = table[i]
    for j in range(nfamily):
        C[0][j + 1] = family[j]
    for m in range(nfamily):
        for n in range(ntable):
            C[m + 1][1 + nfamily + n] = 1
    return C

def arrange_m(F,family,table):
    nfamily = len(family)
    ntable = len(table)
    Arr_m = [[0]*ntable for q in range(nfamily)]
    for i in range(nfamily):
        for j in range(ntable):
            if F[1+nfamily+j][i+1] != 0:
                Arr_m[i][j] = 1
    return Arr_m