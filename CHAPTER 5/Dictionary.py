d = {}  ## Empty Dictionary

Marks = {
    "Abhay" : 100,
    "Alien-X":98,
    "Alien-y":97
}
 
print(Marks)
print(Marks["Abhay"])

# DICTIONARY METHOD
Item = {
    "Banana":10,
    "Mango":20,
    "Guava":30,
}

print(Item.items())

print(Item.keys())

Item.update({"Banana":20})

print(Item.get("Mango"))
print(Item.get("Orange"))  # This will print none

print(Item["Banana"])
# print(Item["Orange"])  # While this one gives error
