from ERGPY import *
from matplotlib import pyplot

# init parser
ergpy = ERGPY()

# parse the demo test run
ergpy.parse('./demoTestRun/ergTest_all.erg')

# generate sample points from Car.v and Car.Road.Route.DevDist
samplePoints = ergpy.getJoinedSamplePoints(['Car.v', 'Car.Road.Route.DevDist'])

# print Car.v when Car.Road.Route.DevDist was greater than 5.81 meters
# also store these values in order to plot them
carV = []
carRoadRouteDevDist = []
for samplePoint in samplePoints:
    if samplePoint['Car.Road.Route.DevDist'] > 5.81:
        print 'Car.v: ' + str(samplePoint['Car.v']) + \
              '   Car.Road.Route.DevDist: ' + str(samplePoint['Car.Road.Route.DevDist'])
        carV.append(samplePoint['Car.v'])
        carRoadRouteDevDist.append(samplePoint['Car.Road.Route.DevDist'])

# plot Car.Road.Route.DevDist over Car.v
pyplot.title('Car.Road.Route.DevDist over Car.v')
pyplot.plot(carV, carRoadRouteDevDist)
pyplot.xlabel('Car.v')
pyplot.ylabel('Car.Road.Route.DevDist')
pyplot.grid(True)
pyplot.show()
