#find the sum of three digit number

num1=int(input('enter any number: '))

n1=num1%10
num2=num1//10

n2=num2%10
num3=num2//10

n3=num3%10
num4=num3//10

ts=n1+n2+n3

print('the total sum of three digit number is: ',ts)
