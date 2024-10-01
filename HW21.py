# Author: Emmalyn Holmquist
# Date: 9/6/2024
# CPSC 507
# HW 2, Problem 1

# Write a function that checks if a number is divisible by 5 or not.
# If it was, returns "Yes, it is!" , and if it wasn't, return "No, it is not!"

def divisible(x): #define function
    if x % 5 == 0: #test using remainder
        print("Yes, it is!")
    else:
        print("No, it is not!")

#divisible(25) #checking code
#divisible(32)