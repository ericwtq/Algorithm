import getadjancy
import Dijksta2D
import DijkstaLL
import Dijsta1D
import getpath


testcase1 = getadjancy.get_matrix("testcase1.txt")
testcase2 = getadjancy.get_array("testcase2.txt")
testcase3 = getadjancy.get_linklist("testcase1.txt")
a1, a2 = Dijksta2D.find_minpath(testcase2)
b1, b2 = DijkstaLL.find_minpath(testcase3)
c1, c2 = Dijsta1D.find_minpath(testcase2)


for i in range(12):
    for j in range(12):
        if i != j :
            print("v",end="")
            print(j+1,end="")
            getpath.print_dijpath(a2,i,j)
            print("<-",end="")
            print("v",end="")
            print(i+1,end="")
            print(", the distance is",end=" ")
            print(a1[i][j])

