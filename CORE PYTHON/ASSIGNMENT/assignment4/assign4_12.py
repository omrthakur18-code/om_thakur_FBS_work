# 12. Write a program to check if given number is Armstrong number or not.

n=int(input('enter any number: '))
count=len(str(n))
temp=n
total=0
while(n>0):
    d=n%10
    total=total+(d**count)
    n=n//10
print(total)
if(total==temp):
    print('number is armstrong')
else:
    print('number is not armstrong')

    
    