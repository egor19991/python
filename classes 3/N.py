import math
number = int(input())
counter = int(0)
if number > 10:
    for i in range(1, int(math.sqrt(number))):
        if number % i == 0:
            counter = counter + 1
        if counter > 1:
            break
elif number <= 10:
    for i in range(1, number):
        if number % i == 0:
            counter = counter + 1
        if counter > 1:
            break
if counter == 1:
    print("YES")
elif number == 1:
    print("NO")
else:
    print("NO")
