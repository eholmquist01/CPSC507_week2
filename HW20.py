# Author: Emmalyn Holmquist
# Date: 9/6/2024
# CPSC 507
# HW 2, Problem 10

# Write a function takes a number grade as its parameter and returns the corresponding letter grade.
# Hint: Check your syllabus for finding the corresponding interval for each letter grade.

#Grades: 93-100 A, 90-92 A-,
# 87-89 B+, 83-86 B, 80-82 B-,
# 77-79 C+, 73-76 C, 70-72 C-,
# 65-69 D+, 55-64 D, 50-54 D-,
# 0-49 F.

def grade(x): #define function
    if 100>x>=93: #set parameters
        return "A" #return letter grade
    elif 93>x>=90:
        return "A-"
    elif 90>x>=87:
        return "B+"
    elif 87>x>=83:
        return "B"
    elif 83>x>=80:
        return "B-"
    elif 80>x>=77:
        return "C+"
    elif 77>x>=73:
        return "C"
    elif 73>x>=70:
        return "C-"
    elif 70>x>=65:
        return "D+"
    elif 65>x>=55:
        return "D"
    elif 55>x>=50:
        return "D-"
    elif 50>x>=0:
        return "F"


print(grade(68)) #check


