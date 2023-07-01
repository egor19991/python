import math
str = input()
numbers = str.split()
n = int(numbers[0])
m = int(numbers[1])
k = int(numbers[2])
result = math.ceil(n * k / m)
print(result)