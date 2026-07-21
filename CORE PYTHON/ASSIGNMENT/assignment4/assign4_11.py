# 11. WAP to check if given number Strong Number.

n=int(input('enter any number: '))
temp=n
sum=0

while temp>0:
   d=temp%10

   fact=1

   for i in range(1,d+1):
         
        fact=fact*i

   sum=sum+fact
   temp=temp//10

if(sum==n):
    print('number is strong.')
else:
    print('number is not strong')