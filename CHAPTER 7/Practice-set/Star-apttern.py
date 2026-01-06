# Write a program to print the following star pattern 

#   *
#  *** 
# *****

n = int(input("Enter a number : "))

for i in range(1, n+1):
    print(" "*(n-i), end = "")   #  This line used to create the spaces n-1 means the spaces from the left , suppose if n=5 then the spaces in first line would be 4 and decrease by 1 till the last line that is 5 

    print("*"*(2*i - 1), end = "") # This line is used to print the starts "*"  the logic part is '2*i-1' , suppose n=5 then for i=1 it will print * and for i = 2 it will print *** and so on till n value  

    print("") 
    
