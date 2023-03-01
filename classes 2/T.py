a = input()
b = input()
c = input()

if "зайка" in a and "зайка" in b and "зайка" in c:
    print(min(a, b, c), len(min(a, b, c)))
elif "зайка" in a and "зайка" in b:
    print(min(a, b), len(min(a, b)))
elif "зайка" in a and "зайка" in c:
    print(min(a, c), len(min(a, c)))
elif "зайка" in b and "зайка" in c:
    print(min(b, c), len(min(b, c)))
elif "зайка" in a:
    print(a, len(a))
elif "зайка" in b:
    print(b, len(b))
elif "зайка" in c:
    print(c, len(c))