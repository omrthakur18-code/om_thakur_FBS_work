# Write a program to check whether the triangle is equilateral, isosceles or scalene triangle.

a=int(input('enter the first side of triangle: '))
b=int(input('enter the second side of triangle: '))
c=int(input('enter the third side of triangle: '))

if(a==b==c):
    print('triangle is eqivalent triangle.')
elif(a==b or b==c or c==a):
    print('triangle is isosceles triangle.')
else:
    print('triangle is scalene triangle.')
    