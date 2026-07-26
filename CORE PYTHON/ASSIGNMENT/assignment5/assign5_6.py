# 6. Write a program to print first n prime numbers.

n=int(input('enter the number: '))

for num in range(2,n+1):
    if(num>1):
        

        for i in range(2,num):
           


           if(num%i==0):

            break
        else:
            print(num)
    else:
       
        print(f'{num} is not prime number nor composite')
        