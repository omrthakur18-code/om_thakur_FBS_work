# Write a program to calculate profit or loss.

costprice=int(input('cost price is: '))
sellingprice=int(input('selling price is: '))

profit=sellingprice-costprice
loss=costprice-sellingprice

if(sellingprice>costprice):
    print('profit: ',profit)
elif(costprice>sellingprice):
    print('loss: ',loss)
else:
    print('no profit,no loss')