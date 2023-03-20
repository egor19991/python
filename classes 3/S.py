message = str("")
a = int(1)
b = int(1000)
while message != "Угадал!":
    c = (b + a) // 2
    print(c)
    message = input()
    if message == "Меньше":
        b = c - 1
    elif message == "Больше":
        a = c + 1