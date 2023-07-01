value = int(input())
n_prime_number = False
for j in range(2, (value // 2) + 1):    
    if (value % j == 0):
        n_prime_number = True
        break
if (value == 1):
    n_prime_number = True
if n_prime_number:
    print("NO")
else:
    print("YES")
