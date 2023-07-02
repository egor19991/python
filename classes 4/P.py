numbers = int(input())
width = int(input())
for i in range(1, numbers + 1):
    text = ""
    for j in range(1, numbers + 1):
        text = text + f"{i * j:^{width}}" + "|"
    print(text[:-1])
    if i < numbers:
        print("-" * (width * numbers + numbers - 1))
