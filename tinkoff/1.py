str = input()
numbers = str.split()
count_plus = 0
count_minus = 0
for i in range(len(numbers) - 1):
    if int(numbers[i]) >= int(numbers[i + 1]):
       count_plus = count_plus + 1
    elif int(numbers[i]) <= int(numbers[i + 1]):
        count_minus = count_minus + 1
if count_minus == 3 or count_plus == 3:
    print("YES")
else:
    print("NO") 