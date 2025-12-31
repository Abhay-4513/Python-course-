# Program to check if the user is eligible for the voting or not 
age = int(input("Enter your age : "))
if(age>=18):
    print("Yes")
    print("Your are eligible for the voting ! ")
elif(age<0):
    print("Please enter a valid age !!")
elif(age<18): 
    print("No")
    print("Your are not eligible for voting......")
