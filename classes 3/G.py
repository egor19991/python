a = int(input())
a1 = a
b = int(input())
b1 = b
while a != 0 and b != 0:
    if a > b:
        a = a % b
    else:
        b = b % a
res = a1 * b1 / (a + b)
print(f"{int(res)}")