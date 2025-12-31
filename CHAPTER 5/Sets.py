f = set()   # This is empty set 
print(type(f))


e = {1,2,3,4,1,1,2,2,5,6,4,4}   # Set print repeated value only ones 
print(e)

#Set methods
s = {1,2,3,4,"Abhay"}

s.add("Grapes")
print(s)

print(len(s))

s.remove(2)
print(s)

s.clear()
print(s)
