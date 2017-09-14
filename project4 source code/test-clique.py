import getgraph
import largestclique
A = getgraph.get_graph("testcase-2.txt")
largestclique.max_clique(A,0)
print("the largest clique is",end=' ')
for i in range(len(A.solution_best)):
    if A.solution_best[i] !=0:
        print(i+1,end=' ')