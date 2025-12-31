# Create an empty dictionary. Allow 4 friends to enter their favourite language as value as key as their names. Assume that the names are unique 
d = {}

name = input("Enter your name : ")
language = input("Enter you favourite language : ")
d.update({name:language})

name = input("Enter your name : ")
language = input("Enter you favourite language : ")
d.update({name:language})

name = input("Enter your name : ")
language = input("Enter you favourite language : ")
d.update({name:language})

name = input("Enter your name : ")
language = input("Enter you favourite language : ")
d.update({name:language})

print(d)
