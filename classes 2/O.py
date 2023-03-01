first = int(input())
second = int(input())
a = first // 10
b = first % 10
c = second // 10
d = second % 10
maximum = max(a, b, c, d)
minimum = min(a, b, c, d)
sum = a + b + c + d - maximum - minimum
result = maximum * 100 + (sum % 10) * 10 + minimum
print(result)