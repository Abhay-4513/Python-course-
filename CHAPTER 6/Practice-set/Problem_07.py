# Write a program to find out whether a given post is talking about "Abhay" or not 


Post = input("Enter your post : ")

if("ABHAY".lower() in Post.lower()):
    print("This post is talking about Abhay")
else:
    print("This post is not talking about Abhay....") 
