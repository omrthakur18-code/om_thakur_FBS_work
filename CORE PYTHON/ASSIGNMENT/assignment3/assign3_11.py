# Accept age of five people and also per person ticket amount and then calculate total
# amount to ticket to travel for all of them based on following condition :
# a. Children below 12 = 30% discount
# b. Senior citizen (above 59) = 50% discount
# c. Others need to pay full.

age1=int(input('enter the age of first person: '))
tiktprice1=int(input('enter the ticket price of first person: '))
totalprice=0

if(age1<12):
    totalprice=totalprice+(tiktprice1*0.30)
elif(age1>59):
    totalprice=totalprice+(tiktprice1*0.50)
else:
    totalprice=totalprice+tiktprice1


    

age2=int(input('enter the age of second person: '))
tiktprice2=int(input('enter the ticket price of second person: '))
totalprice=0

if(age2<12):
    totalprice=totalprice+(tiktprice2*0.30)
elif(age2>59):
    totalprice=totalprice+(tiktprice2*0.50)
else:
    totalprice=totalprice+tiktprice2



age3=int(input('enter the age of third person: '))
tiktprice3=int(input('enter the ticket price of third person: '))
totalprice=0

if(age3<12):
    totalprice=totalprice+(tiktprice3*0.30)
elif(age3>59):
    totalprice=totalprice+(tiktprice3*0.50)
else:
    totalprice=totalprice+tiktprice3



age4=int(input('enter the age of fourth person: '))
tiktprice4=int(input('enter the ticket price of fourth person: '))


if(age4<12):
    totalprice=totalprice+(tiktprice4*0.30)
elif(age4>59):
    totalprice=totalprice+(tiktprice4*0.50)
else:
    totalprice=totalprice+tiktprice4



age5=int(input('enter the age of fifth person: '))
tiktprice5=int(input('enter the ticket price of fifth person: '))


if(age5<12):
    totalprice=totalprice+(tiktprice5*0.30)
elif(age5>59):
    totalprice=totalprice+(tiktprice5*0.50)
else:
    totalprice=totalprice+tiktprice5

print('total price of ticket is ',totalprice)