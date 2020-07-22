# This code stimate the volume of a solid given an (x, y) region
# with back, front, left and right posible function restrictions
# and ceiling and floor z restriction
# It main porpuse is to stimate double integral calculation between
# two functions (f:R^2 -> R) and in different region with 
# x or y restrictions

import numpy as np
import math
from tqdm import tqdm

# Restriction object: a cube in which the solid is in 
class Restriction():

	def __init__(self,x_restriction, y_restriction, z_restriction):

		self.x0, self.x1 = x_restriction
		self.y0, self.y1 = y_restriction
		self.z0, self.z1 = z_restriction

		self.amplitud = [self.x1 - self.x0,
						 self.y1 - self.y0, 
						 self.z1 - self.z0]

		self.volume = self.amplitud[0]*self.amplitud[1]*self.amplitud[2]

	# Return a point inside the cube
	def get_point(self):

		return((np.random.random(3)*self.amplitud)+[self.x0, self.y0, self.z0])

# Solid object: the solid which volume we want to stimate
class Solid():

	def __init__(self, region, f_ceiling, f_floor):

		self.region = region
		self.f_ceiling = f_ceiling
		self.f_floor = f_floor

	# Return True if a given point is inside the solid
	def is_in_solid(self, point):

		x, y, z = point[0], point[1], point[2]

		return (self.region.is_in_region((x,y)) and 
			    self.f_ceiling((x,y)) >= z and 
		        self.f_floor((x,y)) <= z)

# Region object: the (x,y) region where the solid exist
class Region():

	def __init__(self, f_right, f_left, f_back, f_front):

		self.f_left = f_left
		self.f_right = f_right
		self.f_back = f_back
		self.f_front = f_front

	# Return True if a given point is on the region
	def is_in_region(self, point):

		x, y = point[0], point[1]

		return (self.f_back(x) >= y and 
			    self.f_front(x) <= y and
			    self.f_right(y) >= x and 
			    self.f_left(y) <= x)


# region restriction on rigth
def f_right(y):

	return 1

# region restriction on left
def f_left(y):

	return 0

# region restriction on back
def f_back(x):

	return 1

# region restriction on front
def f_front(x):

	return 0

# solid restriction on ceiling
def f_ceiling(point):

	x, y = point[0], point[1]

	return (1/2)*x*(1+y)

# solid restriction on floor
def f_floor(point):

	x, y = point[0], point[1]

	return 0

restriction = Restriction((0,1),(0,1),(0,1)) # Create the restriction cube
region = Region(f_right, f_left, f_back, f_front) # Create the (x,y) region
solid = Solid (region, f_ceiling, f_floor) # Create the solid in 
                                           # the region between two funtions

# This code stimate the volume of the solid using the monte carlo method
# It choose randomly n points inside the restriction cube and check whether
# they are or not in the solid. Knowing the restriction cube volume and
# the number of points that were inside the solid, we can stimate the
# volume of the solid

n_points = 1000000 # number of random points

n_in_solid = 0 # number of points in solid counter

for i in tqdm(range(n_points)):

	random_point = restriction.get_point() # get point from the restriction

	if solid.is_in_solid(random_point): # check if it is inside the solid

		n_in_solid += 1

# calculate the proportion of points in the solid and
# multiply it by the restriction cube volume
print ((n_in_solid/n_points)*restriction.volume) 