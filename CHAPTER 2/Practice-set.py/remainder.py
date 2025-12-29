# Write a program to find the remainder when a numebr is divided by z.....

a = int(input("Enter the Dividend: "))
b = int(input("Enter the Divisor: "))

c = int(a/b)  # Here int is used because by default it gives float like 0.000 so to find remainder we have to covert this into integer
print("The quotient is : ",c)

# Formula to calculate the remainder 
# remainder = dividend - (divisor*quotient)

d = a-(b*c)  # you can also use (a % b)
print("The remainder of the division is : ",d)
