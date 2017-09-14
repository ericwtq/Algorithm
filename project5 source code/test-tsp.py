import getAD
import tsp_heuristic
import tsp_greedy
testcase1_A = getAD.get_adjlist("./tsp/testcase-1")
testcase1_D = getAD.get_matrix("./tsp/testcase-1")
testcase2_A = getAD.get_adjlist("./tsp/testcase-2")
testcase2_D = getAD.get_matrix("./tsp/testcase-2")
testcase1_G = getAD.edge_G("./tsp/testcase-1")
testcase2_G = getAD.edge_G("./tsp/testcase-2")

path_1_h = tsp_heuristic.tsp_heuristic(testcase1_D,testcase1_A,3)
path_2_h = tsp_heuristic.tsp_heuristic(testcase2_D,testcase2_A,3)
path_weight = 0
print("the path is")
for i in path_2_h:
    print(i+1,end = ' ')
    print(">",end = ' ')
print(4)
path_1_h.append(3)
for j in range(len(path_2_h)-1):
    path_weight += testcase2_D[path_2_h[j]][path_2_h[j+1]]
print("the total distance is",end=" ")
print(path_weight)




path_1_g,degree_1_g=tsp_greedy.tsp_greedy(testcase1_G,4)
path_2_g,degree_2_g=tsp_greedy.tsp_greedy(testcase2_G,9)
print("the edge added in to the path is")
print(path_2_g)
print("the degree of each vertice is ")
print(degree_2_g)

