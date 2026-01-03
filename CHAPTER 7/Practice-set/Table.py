# write a program to print the table of any number using for loop

number = int(input("Enter the number : "))

for i in range(11):
    if (i == 0):
        continue
    c = number*i
    print(number ,"X" , i , "= " ,c )

# The upper code is also correct but the simple way is given below 

n = int(input("Enter the number : "))

for i in range(1,11):
    print(f"{n} X {i} = {n*i}")

    # Here (f"") is used so that we can use the variables inside the string 

    # using (1, 11) to start from 1 and not 0 and end at 10
