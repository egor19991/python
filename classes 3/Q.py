number = int(input())
n = len(str(number)) - 1
clean = int(0)
for i in range(n, -1, -1):    
    if (number // 10 ** i) % 2 != 0: 
        clean = clean * 10 + number // 10 ** i
    number = number % 10 ** i
print(clean)