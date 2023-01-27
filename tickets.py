import click
ticket = click.prompt('Укажите кол-во билетов', type=click.IntRange(1, 5)) # Ограничим билеты диапозоном от 1 до 5 штук. 
# ticket = click.prompt('Укажите кол-во билетов', type=int) # Но можно и не ограничивать.
price, i = 0, 0
for i in range(ticket):
            i += 1
            age = click.prompt(f'Возраст {i}-го посетителя', type=click.IntRange(10, 100)) # Ограничим возраст диапозоном от 10 до 100 лет
            if age < 18:
                price += 0
            elif 18 <= age < 25:
                price += 990
            else:
                price += 1390
if ticket > 3:
    discount = 0.9
    print('Сумма к оплате на', ticket, 'чел:', round(discount * price), 'рублёв. С учетом скидки 10 %.')
else:
    discount = 1
    print('Сумма к оплате на', ticket, 'чел:', round(discount * price), 'рублёв')
