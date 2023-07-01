N = int(input())
M = int(input())
text = ""
counter = 1
max_number = len(f"{N * M}") 
for i in range(0, N):
    if i % 2 == 0:
        for j in range(1, M + 1):
            text = text + f"{i * M + j}".rjust(max_number) + " "
    else:
        for j in range(1, M + 1):
            text = text + f"{i * M + j}".rjust(max_number) + " "
    print(text)
    text = ""