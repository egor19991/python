numbers = int(input())
max_numbers = 0
max_name = ""
for i in range(0, numbers):
    name = str(input())
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
    if sum >= max_numbers:
        max_numbers = sum
        max_name = name
print(max_name)