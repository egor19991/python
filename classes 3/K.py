x = int(input())
sum = int(0)
while x > 10:
    sum = sum + x % 10
    x = x // 10
if x == 10:
    sum = sum + 1
else:
    x = x % 10
    sum = sum + x
print(sum)