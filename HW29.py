# Author: Emmalyn Holmquist
# Date: 9/6/2024
# CPSC 507
# HW 2, Problem 9

# Write a function that can take any 5 numbers and returns the average
# of these numbers. Check how your function is working for numbers: 2,23,56,78,901 .

def average(n1, n2, n3, n4, n5): #define function
    sum= n1+ n2 + n3 + n4 + n5 #calc the sum of terms
    nterms =5 #find the number of terms
    return sum/nterms #calc average and return

print(average(2, 23, 56, 78, 901)) #check function