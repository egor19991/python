number = int(input())
sum = int(1)
for i in range(1, number + 1):
    sum = sum * i
if number == int(0):
    print("1")
else:
    print(sum)    