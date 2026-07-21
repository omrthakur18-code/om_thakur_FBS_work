# 5. WAP to print Fibonacci series upto n.

n =int(input('enter fibonacci number you want: '))
a=-1
b=1
c=0

for i in range(n):
    c=a+b
    print(c)

    a=b
    b=c



