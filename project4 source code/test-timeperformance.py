import getgraph
import time
import independentset
import largestclique

A=getgraph.sparse_matrix(34)
startime = time.clock()
independentset.max_independentset(A,0)
endtime = time.clock()
print(endtime - startime)