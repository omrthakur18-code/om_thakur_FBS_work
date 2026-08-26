# with passing parameter without returning value

def addition(num1,num2):           #formal parameter

    sum=num1 + num2

    print(f'addition of {num1} and {num2} is {sum}')


n1=int(input('enter number 1: '))
n2=int(input('enter number 2: '))

addition(n1,n2)             #actual parameter