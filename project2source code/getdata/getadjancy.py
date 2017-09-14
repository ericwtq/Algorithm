from Linklist import LinkedList

def not_empty(s):
    return s and s.strip()
def get_matrix(filename):
    lines = open(filename, 'r').readlines()
    adjancy = [line.strip().split(' ') for line in lines ]
    for i in range(0,len(adjancy)):
        adjancy[i] = list(filter(not_empty,adjancy[i]))
        adjancy[i] = [float('inf') if x == '.' else x for x in adjancy[i]]
        adjancy[i] = [int(x) if x != float('inf') else x for x in adjancy[i]]
        adjancy[i][i] = 0
    return adjancy

def get_array(filename):
    array_temp = get_matrix(filename)
    array_final = [0] * int(((1 + len(array_temp)) * len(array_temp) / 2))
    k = 0
    for i in range(0,len(array_temp)):
        for j in range(0,i + 1):
            array_final[k] = array_temp[i][j]
            k = k + 1
    return array_final

def get_linklist(filename):
    matrix_temp = get_matrix(filename)
    a = LinkedList()
    for i in range(0,len(matrix_temp)):
        b = LinkedList()
        for j in range(0,len(matrix_temp)):
            b.append(matrix_temp[i][j])
        a.append(b)
    return a