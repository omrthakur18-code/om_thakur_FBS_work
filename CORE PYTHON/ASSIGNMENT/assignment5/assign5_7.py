# 7. Write a program to solve the following series :


# a. 1! + 2! + 3! + 4! + .....n!

n=int(input('enter the last digit of number series:  '))
total=0

for i in range(1,n+1):
    fact=1
    for j in range(1,i+1):
        fact*=j
    total+=fact
print(f'the sum of factorial series upto {n} is {total}')


# b. N + N^2 + N^3+N^4 .....+N^N (here ^ means exponent)

N=int(input('enter the number: '))
total=0

for i in range(1,n+1):
    n=N**i
    total+=n
print(f'the sum of given number series is {total}')


# c. Find the sum of a geometric series from 1 to n where the common ratio is 2.

n=int(input('enter the number: '))
total=0
r=2

for i in range(1,n+1):
    s=r**(i-1)
    total+=s
print('the sum of geometric series is: ',total)

# d. S = a + a2 / 2 + a3 / 3 + ...... + a10 / 10

a=int(input('enter the value: '))
total=0

for i in range(1,11):
    s=(a**i)/i
    total+=s
print('the sum of the given series is: ',total)

# e. x - x2/3 + x3/5 - x4/7 + .... to n terms

x=int(input('enter the number: '))
n=int(input('enter the last term: '))
den=1
sign=1
sum=0
for i in range(1,n+1):
    sum=sign*(x**i)/den
    den+=2
    sign+=-1
print(f'sum of series ={sum}')