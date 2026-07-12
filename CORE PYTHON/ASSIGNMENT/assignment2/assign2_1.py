# convert the time entered into hh,min and sec

seconds=int(input('enter time in seconds '))

hh=seconds//3600
sec=seconds%3600

min=sec//60
sec=sec%60

sec=seconds%60


print(f'hours:{hh},minutes:{min},seconds{sec}')