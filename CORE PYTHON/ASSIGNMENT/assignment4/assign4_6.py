# 6. WAP to check if a given number is prime number or not.

num=int(input('enter any number: '))

if(num>1):

    for i in range(2,num//2+1):
        

        if(num%i==0):
           
           print(f'{num} is not prime number')
           break
    else:
        print(f'{num} is prime number')
            
else:
     
     print(f'{num} is not prime number')

