N = int(input())
M = int(input())
text = ""
counter = 1
max_number = len(f"{N * M}") 
for i in range(1, N + 1):     
    for j in range(0, M):
        text = text + f"{i + j * N}".rjust(max_number) + " "
    print(text)
    text = ""