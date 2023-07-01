numbers = int(input())
sum_numbers = 0
for i in range(0, numbers):
    x = int(input())
    sum = 0
    while x > 10:
        sum = sum + x % 10
        x = x // 10
    if x == 10:
        sum = sum + 1
    else:
        x = x % 10
        sum = sum + x
    sum_numbers = sum_numbers + sum
print(sum_numbers)