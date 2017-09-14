import getadjancylist
import dep_check
import bre_check
testcase1, n1 = getadjancylist.get_adjlist("problem_2/testcase1.txt")
testcase2, n2 = getadjancylist.get_adjlist("problem_2/testcase2.txt")
testcase3, n3 = getadjancylist.get_adjlist("problem_2/testcase3.txt")

print("testcase1:")
dep_check.dep_bip(testcase1,n1)
print("testcase2:")
dep_check.dep_bip(testcase2,n2)
print("testcase3:")
dep_check.dep_bip(testcase3,n3)


print("testcase1:")
bre_check.bre_bip(testcase1,n1)
print("testcase2:")
bre_check.bre_bip(testcase2,n2)
print("testcase3:")
bre_check.bre_bip(testcase3,n3)