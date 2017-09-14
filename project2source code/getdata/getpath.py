def print_flopath(P,i,j):
    if P[i][j] > 0 :
        print_flopath(P,i,P[i][j])
        print_flopath(P,P[i][j],j)
    else:
        print("->", end="")
        print("v", end="")
        print(j+1, end="")

def print_dijpath(P,i,j):
    if P[i][j] >0:
        print("<-", end="")
        print("v", end="")
        print(P[i][j]+1, end="")
        print_dijpath(P,i,P[i][j])

