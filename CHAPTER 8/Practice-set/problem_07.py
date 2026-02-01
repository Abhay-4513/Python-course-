# Write a python program to print the multiplication table of given number using function.....


def multiplication(n):
    for i in range(1,11):
        print(f"{n} X {i} = {n*i}")

n = int(input("Enter a number : "))
f = multiplication(n)
