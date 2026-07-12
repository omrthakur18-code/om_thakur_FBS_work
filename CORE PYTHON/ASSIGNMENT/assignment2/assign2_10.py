# wap to reverse three digit number

num=int(input('enter any three digit number: '))

print('before reverse number: ',num)

ones=num%10
num=num//10

tens=num%10
num=num//10

hundred=num%10
num=num//10

reverse=ones*100+tens*10+hundred

print('after reversing the number: ',reverse)