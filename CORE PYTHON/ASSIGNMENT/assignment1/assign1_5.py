#wap to enter p,t,r and calculate compund interest

p=int(input('enter principal amount: '))
t=int(input('enter time: '))
r=int(input('enter rate of interest: '))

amount=p*(1+r/100)**t
CI=amount-p

print('compound interest on given data is ',CI)
