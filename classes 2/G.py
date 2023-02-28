number = int(input())
if (number // 1000 == number % 10) and (number % 1000 // 100 == number % 100 // 10):
    print("YES")
else:
    print("NO")