# Write a program to check if person is eligible to marry or not (male age >=21 and female age>=18)

gender=input('enter the gender of person(m/f): ')
age=int(input('enter the age: '))

if(gender=='f'):
    if(age>=18):
        print('girl is eligible for marriage.')
    else:
        print('girl is not eligible for marriage')
else:
    if(age>=21):
        print('boy is eligible for marriage. ')
    else:
        print('not eligible for marriage.' )