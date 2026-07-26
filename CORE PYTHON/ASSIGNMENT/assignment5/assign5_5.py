# 5. Write a program to print prime numbers between 1 to 100.

for num in range(2,101):
    if(num>1):

        for i in range(2,num):
           


           if(num%i==0):

            break
        else:
            print(num)
    else:
       print(f'{num} is not prime number nor composite')
       

                      