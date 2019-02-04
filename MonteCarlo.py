# -*- coding: utf-8 -*-
"""
Created on Thu Jan 24 23:09:44 2019

@author: Mathieu
"""
import math
import matplotlib.pyplot as plt
import random
import numpy

    # Create random points and order it in 2 lists:
    # pointsInside : For points in the disk
    # pointsOutside : For points out of the disk
    # also returns the ratio Number of points on the disk/total points generated
def Tirage(n):
    xpointsInside = []
    ypointsInside = []
    xpointsOutside = []
    ypointsOutside = []
    kn = 0
    for i in range (0, n):
      point = [random.random(), random.random()]
      if point[0]**2 + point[1]**2 <= 1:
          xpointsInside.append(point[0])
          ypointsInside.append(point[1])
          kn += 1
      else:
          xpointsOutside.append(point[0])
          ypointsOutside.append(point[1])
    return xpointsInside, ypointsInside, xpointsOutside, ypointsOutside, kn/n

    # Shows the points inside and outside of the disk
        # n : number of Tirage(n)'s calling method
def DiskGraph(n):
    xInside, yInside, xOutside, yOutside, ratio = Tirage(n)
    theta = numpy.linspace(0, 2*numpy.pi, 40)
    x = numpy.cos(theta)
    y = numpy.sin(theta)
    plt.scatter(xInside,yInside,s=22)
    plt.scatter(xOutside,yOutside,s=22)
    plt.plot(x, y , color = 'black')
    plt.xlim(0, 1)
    plt.ylim(0, 1)
    plt.title('Monte-Carlos s Disk')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()
    
    # Estimate pi with Monte Carlo method
        # n : number of Tirage(n)'s calling method
def MonteCarlo(n):
    return 4*Tirage(n)[4]

    # Shows the difference between pi and Monte Carlo s estimation
        # begin : smallest point value
        # end : biggest point value
def MonteCarloComparedToPi(begin, end):
    x=[]
    y=[]
    for i in range (begin, end + 1):
        x.append(i)
        y.append(math.pi - MonteCarlo(i))
    plt.scatter(x, y, s=10, label="difference between PI and Monte-Carlo estimation")
    plt.legend()
    plt.xlim(begin, end)
    plt.ylim(0, 0.1)
    plt.xlabel('Point Number')
    plt.ylabel('Pi - estimation')
    plt.show()