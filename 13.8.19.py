Final_price = 0
Tickets=int(input('Введите общее количество билетов:'))
Age=[int(input('Введите возраст каждого посетителя:')) for i in range(Tickets)]

for i in Age:
    if i<18:
        price=0
    elif 18<=i<25:
        price=990
    else:
       price=1390
    Final_price = Final_price+price

print('Вы заказали, билетов:',int(Tickets))
print('Общая стоимость билетов составит:', Final_price,'рублей')
if Tickets>=3:
  print('Общая стоимость билетов c учетом скидки составит:', Final_price*0.9,'рублей')
