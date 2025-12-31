# Write a program to find out whether a student has passed or failed if it requires a total 40% and at least 33% in each subject to pass. 
#Assume 3 subjects and take marks as an input from the user.
mark1 = int(input("Enter marks of Mathematics : "))
mark2 = int(input("Enter marks of Physics : "))
mark3 = int(input("Enter marks of Python : "))
Total = mark1+mark2+mark3
percentage = Total/3
print("------------------------------------------")
print()
if(mark1>=33 and mark2>=33 and mark3>=33 and percentage>=40):
    print("Your are pased")
else:
    print("You must score 33 or above in each subject")
    print("Your are failed")
print()
print("Your total score is : ",Total)
print("Your percentaeg is : ",percentage)
print("------------------------------------------")
