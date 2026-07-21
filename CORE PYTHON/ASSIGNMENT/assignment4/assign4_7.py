# 7. WAP to print all integers upto n that aren’t divisible by 2 and 3.

n=int(input('enter number upto: '))

for i in range(1,n+1):
    if(i%2==1 and i%3==1):

        print(i)
#         print('number is not divisible by 2 and 3')
# else:
#     print('divisible by 2 and 3')
