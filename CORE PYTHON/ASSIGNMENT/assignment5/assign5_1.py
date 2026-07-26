# 1. Write a program to prompt user to enter userid and password. If Id and
# password is incorrect give him chance to re-enter the credentials. Let him try 3
# times. After that program to terminate.


attempt=3

while(attempt>0):

    
    id=input('enter userid: ')
    passw=input('enter password: ')

    if (id=='virat' and passw=='1234'):
        print('login successfully....')
        break
    else:
        attempt=attempt-1
        if(attempt>0):
            print('try again.')
        else:
            print('maximum attempts.')
            print('program terminated.' )


