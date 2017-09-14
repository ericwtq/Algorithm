import  family_table
import format_matrix
import numpy

f = [3,3,2]
t = [4,2,1,3]
C = format_matrix.flow_m(t,f)
maxflow_m,maxflow = family_table.max_flow_2F(0,len(C)-1,C,len(C))
arrange = format_matrix.arrange_m(maxflow_m,f,t)
print("the total people is",end=" ")
print(sum(f))
print("the maxflow is",end=" ")
print(maxflow)
print("the arrangement matrix is ")
print(numpy.matrix(arrange))