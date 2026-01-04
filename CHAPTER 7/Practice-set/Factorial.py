# Write a program to find the factorila of given number using for loop

n = int(input("Enter a number : "))

factorial = 1
for i in range(1, n+1):
    factorial = factorial * i

print(factorial)
