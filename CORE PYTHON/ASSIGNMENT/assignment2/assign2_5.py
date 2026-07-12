# wap to calculate selling price of books based on cost price and discount

cp=int(input('enter the cost price: '))
dis=int(input('enter discont: '))

disamount=cp*dis/100
sp=cp-disamount

print('the selling price of book is ',sp)