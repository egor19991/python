N = int(input())
M = int(input())
text = ""
counter = 0
max_number = len(f"{N * M}") 
for i in range(1, N * M + 1):    
    text = text + f"{i}".rjust(max_number) + " "
    counter = counter + 1
    if counter == M:
        print(text)
        text = ""
        counter = 0