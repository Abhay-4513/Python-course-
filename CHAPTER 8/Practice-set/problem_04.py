# Write a program to print the following star pattern using function....
# ***
# **
# *

def PATTERN(n):
    if(n==0):
        return
    print("*" * n)
    PATTERN (n-1)

n = int(input("Enter the number : "))
PATTERN((n))
