List = [] # Empty list
print(type(List))

NON_HOMOGENEOUS = ["Abhay",328,True]
print(NON_HOMOGENEOUS)
print(NON_HOMOGENEOUS[0])

NON_HOMOGENEOUS[1] = "New name "
print(NON_HOMOGENEOUS[1])


# List is mutable that the changes are being made in the list will print the changed list not a new list .....
Car = ["Lamborghini","Bugatti","Porsche","MC-laren"]
Number = [1,2,3,4,6,8,9,5,7]

Number.sort() # Sort the list
print(Number)

Number.reverse() # Print from last index (-1)
print(Number)

Car.append("Scorpio")
print(Car)

Car.insert(0,"Scorpio")
print(Car)

Number.pop(2)
print(Number)

Number.remove(9)
print(Number)

