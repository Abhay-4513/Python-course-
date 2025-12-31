# A spam comment is defined as a text containing following keywords:
# "Make a lot of money ","buy now ", "subscribe this","click this"
# Write a program to detect these spams..

spm1 = "Make a lot of money"
spm2 = "buy now"
spm3 = "subscribe this"
spm4 = "click this"

Message = input("Enter your message : ")

if((spm1 in Message) or (spm2 in Message) or (spm3 in Message) or (spm4 in Message)):
    print("This message is spam !!")
else:
    print("This message is not spam....")
