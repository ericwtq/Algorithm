import getadjancy
import Floyd1D
import Floyd2D
import FloydLL
import getpath
from memory_profiler import profile


#testcase1 = getadjancy.get_array("testcase1.txt")
testcase2 = getadjancy.get_matrix("testcase2.txt")
#testcase3 = getadjancy.get_linklist("testcase2.txt")
a1, a2 = Floyd2D.find_minpath(testcase2)
#b1, b2 = Floyd1D.find_minpath(testcase1)
#c1, c2 = FloydLL.find_minpath(testcase3)


#for i in range(12):
 #   for j in range(12):
  #      if i != j:
   #         print("v",end="")
    #        print(i+1,end="")
     #       getpath.print_flopath(a2,i,j)
      #      print(", distance is",end=" ")
       #     print(a1[i][j])

