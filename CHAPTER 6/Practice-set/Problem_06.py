# Write a program to calculate the grade of a student from his marks from the following scheme....

mark1 = int(input("Enter marks of Mathematics : "))
mark2 = int(input("Enter marks of Physics : "))
mark3 = int(input("Enter marks of Python : "))
Total = mark1+mark2+mark3
percentage = Total/3

print("Your percentahe is : ",percentage)
if(percentage>90):
    print("Your are Excellent !")
elif(percentage>80):
    print("Your Grade is : A")
elif(percentage>70):
    print("Your Grade is : B")
elif(percentage>60):
    print("Your Grade is : C")
elif(percentage>50):
    print("Your Grade is : D")
elif(percentage<50):
    print("Your Grade is : F")
