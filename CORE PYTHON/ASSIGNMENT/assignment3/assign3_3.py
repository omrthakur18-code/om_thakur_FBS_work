# Write a program to input angles of a triangle and check whether triangle is valid or not.

a=int(input('enter first angle of triangle: '))
b=int(input('enter second angle of triangle: '))
c=int(input('enter third angle of triangle: '))

if(a+b+c==180):
    print('triangle is valid.')
else:
    print('triangle is invalid.')
