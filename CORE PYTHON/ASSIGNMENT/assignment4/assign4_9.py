# 9. WAP to print all numbers in a range divisible by a given number.

n=int(input('enter the number divisible by: '))
r=int(input('enter the range upto: '))

for i in range(1,r+1):
    if(i%n==0):
        print(i)