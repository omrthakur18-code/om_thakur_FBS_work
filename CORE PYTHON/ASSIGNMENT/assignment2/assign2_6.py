#wap to calculate the total salary of employee based on basics,da,hra,ta

bs=int(input('enter the basic salary of employee : '))

da=bs*10/100
ta=bs*12/100
hra=bs*15/100

ts=bs+da+ta+hra

print('total salary of a employee is ',ts)
