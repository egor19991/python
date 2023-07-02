N = int(input())
M = int(input())
text = ""
counter = 1
max_number = len(f"{N * M}") 
for i in range(0, N):
    for j in range(1, M + 1):
        if j % 2 == 0:
            text = text + f"{N * j - i}".rjust(max_number) + " "
        else:
            text = text + f"{N * (j - 1) + 1 + i}".rjust(max_number) + " "
    print(text)
    text = ""