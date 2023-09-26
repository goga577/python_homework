product1=input('Товар1:')
product2=input('Товар2:')
product3=input('Товар3:')
suma=int(product1)+int(product2)+int(product3)
if product1 < product2 and product2 < product3:
    print('Акция!',int(suma)/2)
elif product1>product2 and product2>product3:
    print('Акция!', int(suma)/3)
else:
    print('К оплате:')