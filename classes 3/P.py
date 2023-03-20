number = int(input())
n = len(str(number)) - 1
for i in range(n, 1, -2):
    if number // (10 ** i) != number % 10:
        print("NO")
        exit()
    number = number % (10 ** i)
    number = number // 10
print("YES")