import getadjancylist
import checkcycle

testcase1, n1 = getadjancylist.get_adjlist("problem_1/testcase1.txt")
testcase2, n2 = getadjancylist.get_adjlist("problem_1/testcase2.txt")
testcase3, n3 = getadjancylist.get_adjlist("problem_1/testcase3.txt")

print("testcase1:")
checkcycle.check_cyl(testcase1,n1)

print("testcase2:")
checkcycle.check_cyl(testcase2,n2)

print("testcase3:")
checkcycle.check_cyl(testcase3,n3)