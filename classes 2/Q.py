import math
a = float(input())
b = float(input())
c = float(input())
D = math.pow(b, 2) - 4 * a * c

if a == 0 and b == 0 and c == 0:
    print("Infinite solutions")
elif a == 0 and b != 0 and c != 0:
    x1 = -(c / b)   
    print(x1)
elif a == 0 and b == 0 and c != 0:
    print("No solution")
elif a == 0 and b != 0 and c == 0:
    x1 = 0
    print(x1)
else:
    D = math.pow(b, 2) - 4 * a * c
    if (D > 0):
        x1 = (-b - math.sqrt(D)) / (2 * a)
        x2 = (-b + math.sqrt(D)) / (2 * a)
        print("%.2f" % min(x1, x2), "%.2f" % max(x1, x2))
    elif D == 0:
        x = -b / (2 * a)
        print("%.2f" % x)
    elif D < 0:
        print("No solution")