# 2. Enter number of students from user. For those many students accept marks of 5
# subject marks from user and calculate percentage. Display all percentage and
# average percentage of students.

num=int(input('enter number of students: '))
temp=num

totalpercentage=0

while(temp>0):
    s1=int(input('enter marks in first subject: '))
    s2=int(input('enter marks in second subject: '))
    s3=int(input('enter marks in third subject: '))
    s4=int(input('enter marks in fourth subject: '))
    s5=int(input('enter marks in fifth subject: '))

    percentage=((s1+s2+s3+s4+s5)/500)*100

    print('percentage of student is ',percentage)

    totalpercentage=totalpercentage+percentage

    temp=temp-1

    

avgper=totalpercentage/num
print('average percentage of students is: ',avgper)
