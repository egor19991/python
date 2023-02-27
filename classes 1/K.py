number = int(input())
reverese_number = (number // 100 % 10) * 1000 + (number // 1000) * 100 + (number % 10) * 10 + number // 10 % 10
print(reverese_number)