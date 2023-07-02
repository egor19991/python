numbers = int(input())
sum = 0
for j in range(numbers):
    n_polindrom = False
    number = int(input())
    n = len(str(number)) - 1
    for i in range(n, 1, -2):
        if number // (10 ** i) != number % 10:
            n_polindrom = True
            break
        number = number % (10 ** i)
        number = number // 10
    if n_polindrom is False:
        sum = sum + 1
print(sum)