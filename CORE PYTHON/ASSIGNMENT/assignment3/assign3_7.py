# Write a program to check if user has entered correct userid and password.

userid=input('enter the userid= ')
password=input('enter the password= ')

if(userid=='admin' and password=='virat@18'):
    print('user login successfully.')
else:
    print('user is invalid.')