# ERGpy
##### Description
Pure python parser to use result files from carMaker in python.

##### Notes
* Both files .erg and .erg.info are needed to parse the results.
* The parsed values for each quantity are in the right chronological order.


---


## Installation
Just clone this repository and run in the same directory:

```
python setup.py install
```
This script installs ERGpy and the required libs numpy and matplotlib.

---

## Usage
### Parse
It couldnt be any easier to parse the result files - just one line of code is needed.


```python
quantities = ERGPY().parse('.\demoTestRun\ergTest_all.erg')
```
The parse function returns all found quantities in the right order.

For example

```
#!python

quantities=[
   {
      name = 'Car.v',
      values = [
         25.0,
         26.7
      ]
   }
]
```

### Get desired quantitys
ERGpy is also able to get only the values of a desired quantity:

```python
# get only the velocity values
carV = ergpy.getSingleQuantityValues('Car.v')
```

### Work with sample Points
A sample is an object containing all needed quantities at a discret time.
ERGpy can easily generate sample points from a list of desired quantities.

```python
# generate sample points from Car.v and Car.Road.Route.DevDist
samplePoints = ergpy.getJoinedSamplePoints(['Car.v', 'Car.Road.Route.DevDist'])
```