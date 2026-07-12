

i=int(input('enter any amount: '))

n1=i//2000
i=i%2000

n2=i//500
i=i%500

n3=i//200
i=i%200

n4=i//100
i=i%100

n5=i//50
i=i%50

n6=i//20
i=i%20

n7=i//10
i=i%10

min=n1+n2+n3+n4+n5+n6+n7

print(f'notes of 2000:{n1}, 500:{n2}, 200:{n3}, 100:{n4}, 50:{n5}, 20:{n6}, 10:{n7}')
print('minimum amount of notes required is: ',min)