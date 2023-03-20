counter = int(0)
n = int(input())
for i in range(n):
    name = input()
    if "зайка" in name:
        counter = counter + 1
print(counter)