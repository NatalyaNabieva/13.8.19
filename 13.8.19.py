Tickets=int(input('Введите количество билетов:'))
Age=[int(input('Введите возраст каждого посетителя:')) for i in range(Tickets)]
listMask = []
for i in Age:
    if i<18:
        listMask.append(0) 
    elif 18<=i<25:
         listMask.append(990)
    else:
         listMask.append(1390) 
Final_price=sum(listMask)
print('Вы заказали, билетов:',int(Tickets))
print('Стоиомсть билетов:',(listMask),'рублей') 
if Final_price>=2970 and int(Tickets)>=3:  
    print('Общая стоимость билетов c учетом скидки:',Final_price*0.9,'рублей')
else:
    print('Общая стоимость билетов составит:',Final_price,'рублей')
