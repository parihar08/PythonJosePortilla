#1. Fill in the Line class methods to accept coordinates as a pair of tuples and return the
#slope and distance of the line
import math

class Line():

    def __init__(self,coor1,coor2):
        self.coor1 = coor1
        self.coor2 = coor2

    def distance(self):

        # x1,y1 = self.coor1  #Tuples Unpacking
        # x2,y2 = self.coor2
        # return ((x2-x1)**2 + (y2-y1)**2)**0.5
        distance = (self.coor2[0] - self.coor1[0])**2 + (self.coor2[1] - self.coor1[1])**2
        return math.sqrt(distance)

    def slope(self):
        slope = (self.coor2[1] - self.coor1[1])/(self.coor2[0] - self.coor1[0])
        return slope

coordinate1 = (3,2)
coordinate2 = (8,10)

li = Line(coordinate1,coordinate2)

print('Distance between 2 coordinates is',li.distance())

print('Slope of 2 coordinates is',li.slope())

print('*********************************************')

#2. Find Volume and Surface area of Cylinder

class Cylinder:

    pi = 3.14

    def __init__(self,height=1,radius=1):
        self.height = height
        self.radius = radius

    def volume(self):
        return self.pi*(self.radius**2)*self.height

    def surface_area(self):
        return (2*self.pi*self.radius*self.height) + (2*self.pi*self.radius**2)

c = Cylinder(2,3)

print('Volume of Cylinder is',c.volume())

print('Surface Area of Cylinder is',c.surface_area())