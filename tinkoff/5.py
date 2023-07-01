length = int(input())
str = input()
count = 0
numbers = str.split()
int_numbers = [int(x) for x in numbers]
for i in range(length):
    sum = 0
    for j in range(i, length):
        sum = sum + int_numbers[j]
    if sum == 0:
        count = count + 1
print(count)