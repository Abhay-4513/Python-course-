# Tupple : It is the combination of string and list .....
# Tupple = Immutable + List of different data types 


Tuple = ()
print(type(Tuple))


a = (1,2,"Abhay","Scorpio")   # To know the tupple either use () or (any thing ,)
           # Without 'comma' it will conside it as another type 
print(a)
print(type(a))

b =(34,54,"Abhay","Mango","New tuple")

print(b)

New_Tupple = b.count(54)
print(New_Tupple)

Tupple = b.index(34)
print(Tupple)
