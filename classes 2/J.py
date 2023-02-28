number = int(input())
a = number // 100 + number // 10 % 10
b = number // 10 % 10 + number % 10
total = str(max(a, b)) + str(min(a, b))
print(total)