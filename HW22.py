# Author: Emmalyn Holmquist
# Date: 9/6/2024
# CPSC 507
# HW 2, Problem 2

# Write a function that compares three different numbers and returns the maximum.
# Call your function for 2, 25, and 17 . Note: Do not use max built-in function.

def find_max(n1, n2, n3): #define function
    if n1 > n2 and n1 > n3: #if n1 is greater than both numbers, it is the max. return it
        return n1
        #print("max is: ", n1) #used print statements to check
    elif n2>n1 and n2>n3: #repeat for n2
        return n2
        #print("max is: ", n2)
    else:           #if n1 is not the max and n2 is not the max, n3 must be. return it
        return n3
       # print("max is: ", n3)

find_max(2, 25, 17)

