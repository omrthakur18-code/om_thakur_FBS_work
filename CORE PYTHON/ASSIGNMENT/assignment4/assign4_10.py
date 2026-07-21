# 10. WAP to check if given number is Perfect Number.

n=int(input('enter any number: '))
sum=0

for i in range(1,n):
    if(n%i==0):
        sum=sum+i

if(sum==n):
    print('number is perfect')
else:
    print('number is not perfect')

    