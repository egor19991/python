numbers = int(input())
sum_numbers = ""
for i in range(numbers):
    x = int(input())
    max_number = 0
    while x > 10:
        if x % 10 > max_number:
            max_number = x % 10
        x = x // 10
    if x < 10 and x > max_number:
        max_number = x
    sum_numbers = sum_numbers + f"{max_number}"
print(sum_numbers)