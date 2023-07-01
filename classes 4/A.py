numbers = int(input())
for i in range(1, numbers + 1):
    text = ""
    for j in range(1, numbers + 1):
        text = text + f"{i * j} "
    print(text[:-1])