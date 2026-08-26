def pallindrome():
    n=int(input('enter any number: '))
    temp=n
    rev=0

    while temp>0:
        d=temp%10
        temp=temp//10
        rev=rev*10+d

    if(n==rev):
        print('the number is pallindrome')
    else:
        print('the number is not pallindrome')

pallindrome()
