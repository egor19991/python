product_name = input()
price = float(input())
weight = float(input())
money = float(input())
total = money - weight * price
sum = weight * price
print('Чек')
print(f'{product_name} - {int(weight)}кг - {int(price)}руб/кг')
print(f'Итого: {int(sum)}руб')
print(f'Внесено: {int(money)}руб')
print(f'Сдача: {int(total)}руб')