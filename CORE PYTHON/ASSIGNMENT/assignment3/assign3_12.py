# 12. Write a program to check if given 3 digit number is a palindrome or not.

num=int(input('enter three digit number: '))

if(num>=100 and num<=999):
    first=num//100
    last=num%10
    if(first==last):
        print('number is palindrome.')
    else:
        print('number is not palindrome.')
else:
    print('number is invalid.')

    