import numpy as np
import random
from Linklist import LinkedList

def complete_array(n):
    carray = list(np.random.randint(1,n,size=(1+n)*n//2))
    for i in range(0,n):
        carray[i+(i+1)*i//2] = 0
    return carray

def complete_matrix(n):
    carray = complete_array(n)
    cmatrix = [[0 for col in range(n)] for row in range(n)]
    for i in range(0,n):
        for j in range(0,n):
            i_max_j = max(i,j)
            i_min_j = min(i,j)
            cmatrix[i][j] = carray[i_min_j+(1+i_max_j)*i_max_j//2]
    return cmatrix

def complete_linklist(n):
    cmatrix = complete_matrix(n)
    a = LinkedList()
    for i in range(0,n):
        b = LinkedList()
        for j in range(0,n):
            b.append(cmatrix[i][j])
        a.append(b)
    return a


def sparse_array(n):
    topv = []
    sarray =[float("inf")]*((1 + n) * n // 2)
    allv = [i for i in range((1 + n) * n // 2)]
    for i in range(0, n):
        sarray[i + (i + 1) * i // 2] = 0
        topv.append(i + (i + 1) * i // 2)
    for j in topv:
        allv.remove(j)
    r = random.sample(allv,n-1)
    for k in r:
        sarray[k] = np.random.randint(1,n)
    return sarray


def sparse_matrix(n):
    sarray = sparse_array(n)
    smatrix = [[0 for col in range(n)] for row in range(n)]
    for i in range(0, n):
        for j in range(0, n):
            i_max_j = max(i, j)
            i_min_j = min(i, j)
            smatrix[i][j] = sarray[i_min_j + (1 + i_max_j) * i_max_j // 2]
    return smatrix


def sparse_linklist(n):
    smatrix = sparse_matrix(n)
    a = LinkedList()
    for i in range(0, n):
        b = LinkedList()
        for j in range(0, n):
            b.append(smatrix[i][j])
        a.append(b)
    return a