# Write a program to print the sum of first n natural numbers using the recursion function....

def nSum(n1):
    if(n1==1):
        return 1
    return nSum(n1-1)  + n1     

'''
lets understand the logic behind the calculation nSUm(n1-1)+n1
let's consider the value is 10 
so the first step will be nSum(10) = nSum(9)+10
step second nSum(9) = nSum(8)+9
step third nSum(8) = nSum(7)+8
step four nSum(7) = nSum(6)+7
step five nSum(6) = nSum(5)+6
step six nSum(5) = nSum(4)+5
step seven nSum(4) = nSum(3)+4
step eight nSum(3) = nSum(2)+3
step nine nSum(2) = nSum(1)+2
step ten nSum(1) = return 1

now go backward 
nSum(2) = 1 + 2 = 3
nSum(3) = 3 + 3 = 6
nSum(4) = 6 + 4 = 10
nSum(5) = 10 + 5 =15
nSum(6) = 15 + 6 = 21
nSUm(7) = 21 + 7 = 28
nSum(8) = 28 + 8 = 36
nSum(9) = 36 + 9 = 45
nSum(10) = 45 + 10 = 55
'''
n1 = int(input("Enter the number : "))

print(f"The sum is : {nSum(n1)}")
