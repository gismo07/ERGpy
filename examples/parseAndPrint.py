from ERGPY import *

# init parser
ergpy = ERGPY()

# parse the demo test run
ergpy.parse('./demoTestRun/ergTest_all.erg')

# get only the velocity values
carV = ergpy.getSingleQuantityValues('Car.v')

# print the first 10 elements
for i in range(0, 11, 1):
    print(carV[i])

