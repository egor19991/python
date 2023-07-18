number = int(input())
sum_numbers = 0
num = 0
for i in range(2, 11):
    sum_number = 0
    cur_number = number
    while cur_number > 0:
        if cur_number >= i:
            sum_number = sum_number + cur_number // i
            cur_number = cur_number - cur_number // i
        else:
            sum_number = sum_number + cur_number % i
            cur_number = cur_number - cur_number % i
    if sum_number > sum_numbers:
        sum_numbers = sum_number
        num = i
print(num)