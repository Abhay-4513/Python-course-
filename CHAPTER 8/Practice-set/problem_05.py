# Write a program to convert the inches into centimeters...
# Formula :-  centimeter = inches * 2.54

def cenInch(centimeter):
    return centimeter * 2.54

centimeter = int(input("Enter the vlaue : "))
c = cenInch(centimeter)
print(f"The conversion of the above value in the centimeters is : {round(c, 2)}")
