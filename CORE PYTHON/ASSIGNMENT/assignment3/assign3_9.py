# Input 5 subject marks from user and display grade(eg.First class,Second class ..)

m1=int(input('enter marks in first subject: '))
m2=int(input('enter marks in second subject: '))
m3=int(input('enter marks in third subject: '))
m4=int(input('enter marks in fourth subject: '))
m5=int(input('enter marks in fifth subject: '))

percentage=(m1+m2+m3+m4+m5)/500*100
print('percentage is: ',percentage)

if(percentage>=80):
    print('pass in first class.')
elif(percentage>=60):
    print('pass in second class.')
elif(percentage>=35):
    print('pass in third class.')
else:
    print('failed')
