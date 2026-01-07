# Function is a group of statements of statements that are used to perform a specific task

def func1():
    a = int(input("Enter a number : "))
    b = int(input("Enter a number : "))

    c = (a+b)/2
    print(f"The average of the above number is : {c}")
    
func1()

# This is fucntion with argument

def GoodDay(name,ending):
    print(f"Good day, {name}  {ending}")
GoodDay(f"Abhay","\nThanks you")
