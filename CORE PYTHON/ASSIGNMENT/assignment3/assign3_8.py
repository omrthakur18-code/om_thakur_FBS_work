# Write a program to prompt user to enter userid and password. After verifying
# userid and password display a 4 digit random number and ask user to enter the
# same. If user enters the same number then show him success message otherwise
# failed. (Something like captcha)


import random

userid=input('enter the userid= ')
password=input('emter the password= ')

if(userid=='admin' and password=='virat@18'):
    captcha=random.randint(1000,9999)
    print(f'your captcha is {captcha}')
    chuser=int(input('enter the captcha= '))
    chuser==captcha
    print('user login successfully.')
else:
    print('user is invalid')