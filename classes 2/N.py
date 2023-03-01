number = int(input())
a = number % 10
b = number // 10 % 10
c = number // 100
maximum = max(a * 10 + b, a * 10 + c, b * 10 + a, b * 10 + c, c * 10 + a, c * 10 + b)
minimum = min(a * 10 + b, a * 10 + c, b * 10 + a, b * 10 + c, c * 10 + a, c * 10 + b)
if (minimum < 10):
    minimum = minimum * 10
print(minimum, maximum)