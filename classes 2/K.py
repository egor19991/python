number = int(input())
a = number % 10
b = number // 10 % 10
c = number // 100
maximum = max(a, b, c)
minimum = min(a, b, c)
avg = a
if a != minimum and a != maximum:
    avg = a
elif b != minimum and b != maximum:
    avg = b
else:
    avg = c

if maximum + minimum == avg * 2:
    print("YES")
else:
    print("NO")