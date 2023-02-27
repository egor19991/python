name = str(input())
price = int(input())
weight = int(input())
money = int(input())
sum = price * weight
sur = money - sum
print("================Чек================")
print("Товар:" + f"{name:>29}")
print("Цена:" + f"{weight}кг * {price}руб/кг".rjust(30))
print("Итого:" + f"{sum:>26}руб")
print("Внесено:" + f"{money:>24}руб")
print("Сдача:" + f"{sur:>26}руб")
print("===================================")