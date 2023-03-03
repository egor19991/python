k = int(input())
n = int(input())
string = str(f"{k}")
if k < n:
    for i in range(k + 1, n + 1):
        string = string + f" {i}"
elif k > n:
    for i in range(k - 1, n - 1, -1):
        string = string + f" {i}"
print(string)