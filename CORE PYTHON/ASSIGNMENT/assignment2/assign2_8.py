#wap to swap two numbers using third variable

x=int(input('enter first number: '))
y=int(input('enter second number: '))

print(f'before swapping x:{x} and y:{y}')

z=x
x=y
y=z

print(f'after swapping x:{x} and y:{y}')