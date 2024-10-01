# Author: Emmalyn Holmquist
# Date: 9/6/2024
# CPSC 507
# HW 2, Problem 6

# Write a function that takes the temperature and if the temperature was above 78
# asks you to turn on the AC and if the temperature was below 62 asks you to turn on the heater.
# For temperature greater than or equal to 62 and less than or equal to 78,
# tells you "it's a wonderful weather!" .


def temp(x): #define function
    if x>78: #set conditionals for evaluating response to temp
        print("Please turn on the AC!")
    elif x<62:
        print("Please turn on the heater!")
    elif 62<=x<=78:
        print("it's a wonderful weather!")


temp(80) #test function
