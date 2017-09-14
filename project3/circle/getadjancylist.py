from collections import defaultdict


def not_empty(s):
    return s and s.strip()


def get_adjlist(filename):
    lines = open(filename, 'r').readlines()
    adjancy = [line.strip().split(' ') for line in lines ]
    n = len(adjancy)
    for i in range(n):
        adjancy[i] = list(filter(not_empty,adjancy[i]))
        adjancy[i] = [0 if x == '.' else 1 for x in adjancy[i]]

    adjlist = defaultdict(list)
    for i in range(n):
        for j in range(n):
            if adjancy[i][j] != 0:
                adjlist[i].append(j)
    return adjlist, n



