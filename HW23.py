# Author: Emmalyn Holmquist
# Date: 9/6/2024
# CPSC 507
# HW 2, Problem 3

# Write a function that compare three di erent numbers and returns the minimum.
# Call your function for 206, 405 and 112 . Note: Do not use min built-in function.

def find_min(n1, n2, n3): #define function
    if n1 < n2 and n1 < n3: #if n1 is less than both numbers, it is the min. return it
        return n1
        #print("max is: ", n1) #used print statements to check
    elif n2<n1 and n2<n3: #repeat for n2
        return n2
        #print("max is: ", n2)
    else:           #if n1 is not the min and n2 is not the min, n3 must be. return it
        return n3
       #print("max is: ", n3)

find_min(206, 405, 112)
