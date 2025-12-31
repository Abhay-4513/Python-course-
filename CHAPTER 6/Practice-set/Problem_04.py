# Write a program to find whether a given username contains less than 10 charcter or not 

Username = input("Enter your username : ")

a = len(Username)

if(a<=10):
    print("Username is accepted")
else:
    print("length is greater than 10")
    
