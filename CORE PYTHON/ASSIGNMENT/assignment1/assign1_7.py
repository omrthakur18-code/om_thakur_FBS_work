# program to find out the roots of quadratic equation

a=int(input('enter the first number: '))
b=int(input('enter the second number: '))
c=int(input('enter the third number: '))

d=b**2-4*a*c
r1=(-b+(d**0.5))/2*a
r2=(-b-(d**0.5))/2*a

print(f'first root of quadratic equation is {r1} and second root of quadratic equation is {r2}')