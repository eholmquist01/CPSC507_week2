# Author: Emmalyn Holmquist
# Date: 9/6/2024
# CPSC 507
# HW 2, Problem 5

# Write a function that calculate the summation of the odd numbers between any two numbers, a and b.
# Check if the function is working for summation of odd numbers between 2 and 14 .
# Hint: You may de ne a function to check if a number is odd and use that function inside your function.

def sumbtwn(x, y): #define function for summing between numbers
    if x + 1 >= y or x >= y: #base case
        return 0

    finalsum = 0 #this initializes the sum

    def oddsum(x1, y1): #define function that determines if odd
        nonlocal finalsum #this pulls the variable "total" from the outside function sumbtwn
        if x1>= y1: #if start is greater than or equal to end, we can stop the function
            return
        if x1 % 2 != 0: #this tests if its odd and adds to the total
            finalsum += x1

        oddsum(x1 + 1, y1) #this increases the integer
    if x < y: #back to og function
        oddsum(x + 1, y) #calculating sum of odd numbers

    else:
        oddsum(y+1, x)

    return finalsum #return the final sum

print(sumbtwn(2, 14)) #check