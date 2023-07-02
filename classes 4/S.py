size = int(input())
text = ""
if size >= 19:
    size_format = 2
else:
    size_format = 1
for i in range(1, size + 1):
    for j in range(1, size + 1):
        if i == 1:
            text = text + f"{1:^{size_format}} "
        if (i > 1) and (i <= (size // 2) + 1):
            if j <= i and j < size + 2 - i:
                text = text + f"{j:^{size_format}} "
            elif j > i and j < size + 2 - i:
                text = text + f"{i:^{size_format}} "
            elif j > (size // 2) + 1:
                text = text + f"{size + 1 - j:^{size_format}} "
        if (i > (size // 2) + 1):
            if j < size + 2 - i:
                text = text + f"{j:^{size_format}} "
            elif j > i:
                text = text + f"{size + 1 - j:^{size_format}} "
            else:
                text = text + f"{size + 1 - i:^{size_format}} "
    print(text)
    text = ""