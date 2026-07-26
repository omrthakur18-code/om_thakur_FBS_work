# 3. Accept no. of passengers from user and per ticket cost. Then accept age of each
# passenger and then calculate total amount to ticket to travel for all of them based on
# following condition :
# a. Children below 12 = 30% discount
# b. Senior citizen (above 59) = 50% discount
# c. Others need to pay full.

n=int(input('enter the no. of passengers: '))
totalamount=0

while(n>0):
    age=int(input('age of passengers: '))
    ticktprice=int(input('enter ticket price: '))

    if(age<12):
        totalamount=totalamount+(ticktprice*0.70)
    elif(age>59):
        totalamount=totalamount+(ticktprice*0.50)
    else:
        totalamount=totalamount+ticktprice

    n-=1

print('total amount of ticket is: ',totalamount)


        