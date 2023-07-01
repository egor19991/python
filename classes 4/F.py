numbers = int(input())
a = int(input())
for i in range(numbers - 1):
    b = int(input())
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    a = a + b
print(a)