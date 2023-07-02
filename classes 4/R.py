numbers = int(input())
numbers_string = 0
last_number = 1
text = ""
max_len = 0
counter = 1
for i in range(1, numbers + 1):
    numbers_string = numbers_string + 1
    text = text + f"{i} "
    if numbers_string == last_number or i == numbers:
        last_number = numbers_string + 1
        max_len = len(text)
        text = ""
        numbers_string = 0
last_number = 1
numbers_string = 0
text = ""
for i in range(1, numbers + 1):
    numbers_string = numbers_string + 1
    text = text + f"{i} "
    if numbers_string == last_number or i == numbers:
        last_number = numbers_string + 1
        print(f"{text:^{max_len}}")
        text = ""
        numbers_string = 0