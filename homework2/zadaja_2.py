price=input('Оплата:')
time=input('Время:')
if time == 10 or 11 or 12:
    print(int(price)//2,time) 
elif time == 20 or 21 or 22:
    print(int(price)//4,time)


