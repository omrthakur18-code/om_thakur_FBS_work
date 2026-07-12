# convert distant given in feet and inches into meter and centimeter

feet=int(input('enter value in feets: '))
inches=int(input('enter value in inches: '))

totalinches=feet*12+inches
cent=totalinches*2.54
metre=cent/100

print(f'inches in centimetre:{cent}, metres:{metre}')
