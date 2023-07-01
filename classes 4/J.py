numbers = int(input())
print("А Б В")
for i in range(1, numbers + 1):
    if i == numbers - 1:
        break
    for j in range(1, numbers + 1):    
        if (numbers - i - j == 0):
            break
        print(f"{i} {j} {numbers - i - j}")