from ERGPY import *
from matplotlib import pyplot

# parse the result file
quantities = ERGPY().parse('.\demoTestRun\ergTest_all.erg')

# index used for the figure numbers
index = 1

# iterate through all quantities and plot them in a single figure
for q in quantities:
    if q.name != '$none$':
        pyplot.figure(index)
        pyplot.plot(q.values)
        pyplot.title(q.name)
        pyplot.grid(True)
        index += 1

# show the plots
pyplot.show()
