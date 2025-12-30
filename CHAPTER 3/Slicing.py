# Negative slicing
Name = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

NegaticeSLICING = Name[-8:-5]
print(NegaticeSLICING)

PositiveSlicing = Name[18:21]   # Convet the negative to positive 
print(PositiveSlicing)

# Skip value slicing
Word = "ABHAYTRIPATHI"

len = Word[0:9:2]
print(len)
