n = int(input())
min_name = input()
for i in range(n - 1):
    input_name = input()
    if (min_name > input_name):
        min_name = input_name
print(min_name)