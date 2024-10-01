# Author: Emmalyn Holmquist
# Date: 9/6/2024
# CPSC 507
# HW 2, Problem 4

# Write a function that takes two numbers and nd the summation of all the numbers between these two numbers.
# Check how your function is working by passing 1 and 5 to it.
# What will you get if you pass 20 and 113 to your function?
# Hint: The function should be able to take, for example, 2 and 7 and returns the summation of 3 +4+5+6,
# which is 18.

def sumbtwn(x, y):
    if x+1 >=y or x>= y: #if y and x are equal, there are no ints between them
        return 0
    elif x<y: #if x <y, then we need to sum counting up from x and down from y
        return (x+1) + sumbtwn(x+1, y)
    else: #if not then y>x, we need to sum counting up from y and down from x
        return (y+1) + sumbtwn(x, y+1)

print(sumbtwn(1, 5)) #check
print(sumbtwn(20, 113))

#With 1, 5, and 20, 113, we get 9 and 6118, respectively.
