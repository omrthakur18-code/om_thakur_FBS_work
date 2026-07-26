# 4. WAP to print Armstrong number within a given range

s=int(input('enter the starting range: '))
e=int(input('enter the ending range: '))
count=int(str(i))

for i in range(s,e+1):
    num=i
    count=int(str(i))
    

    total=0
    temp=num
    while temp>0:
        d=temp%10
        total=total+(d**count)
        temp=temp//10

print(total)
if(total==num):

    print(i)
