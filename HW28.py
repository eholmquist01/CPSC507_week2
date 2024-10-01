# Author: Emmalyn Holmquist
# Date: 9/6/2024
# CPSC 507
# HW 2, Problem 8

# Write a function that takes the longitude and latitude of two points and returns the Euclidean distance
# between them. How many parameters should your function take?
# Hint: the Euclidean distance formula is the distance formula that you have in your slides.

#this problem will need 4 parameters
import math #importing math library

def distance(x1, y1, x2, y2): #define function & num arguments
    dx = x2-x1 #calculate slope for x and y
    dy = y2 - y1
    dsquared = dx**2 + dy**2 #under the radicand
    result = math.sqrt(dsquared) #using math library for square root
    return result

print(distance(1, 1, 2, 2)) #check function