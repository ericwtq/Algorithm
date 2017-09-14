import getgraph
import independentset
A = getgraph.get_graph("testcase-2.txt")
independentset.max_independentset(A,0)
print("the maximal independent set is",end=' ')
for i in range(len(A.solution_best)):
    if A.solution_best[i] !=0:
        print(i+1,end=' ')
