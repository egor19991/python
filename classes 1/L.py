a = int(input())
b = int(input())
c = (a // 100 + b // 100) % 10
d = (a // 10 % 10 + b // 10 % 10) % 10
f = (a % 10 + b % 10) % 10
sum = c * 100 + d * 10 + f
print(sum)