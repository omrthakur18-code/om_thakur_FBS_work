#wpa to swap two numbers without using third variable

x=int(input('enter first number: '))
y=int(input('enter second number: '))

print(f'before swapping x:{x} and y:{y}')

x,y=y,x

print(f'after swapping x:{x} and y:{y}')