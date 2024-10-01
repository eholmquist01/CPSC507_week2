# Author: Emmalyn Holmquist
# Date: 9/6/2024
# CPSC 507
# HW 2, Problem 7

# Use your factorial function and write a function that takes two parameters,
# n and r, and calculates the following formula: P(n, r) = n!/(n-r)!

def factorial(num):
    if not isinstance(num, int): #checking data type: is it an integer?
        print("the Factorial is only defined for integers.")
        return None
    elif num<0: #making sure is not negative
        print("Factorial is not defined for negative integers.")
        return None
    elif num == 0: #case where n = 0
        return 1
    else:
        return num * factorial(num-1) #calculating factorial



def p(n, r):
    if not isinstance(n, int) or not isinstance(r, int): #checking data types again
        return None
    if n<0 or r < 0 or r>n: #if they are negative or will create a negative (denom)
        return None

    num = factorial(n) #calculate num and denom seperately
    denom = factorial(n-r)

    if denom is None: #if denom creates a problem, final check, then we can't return anything
        return None

    return num/denom #return the permutation

print(p(4, 2)) #check
