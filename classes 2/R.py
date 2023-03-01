import math
a = float(input())
b = float(input())
c = float(input())

alpha = (math.pow(a, 2) + math.pow(c, 2) - math.pow(b, 2)) / (2 * a * c)
beta = (math.pow(a, 2) + math.pow(b, 2) - math.pow(c, 2)) / (2 * a * b)
gamma = (math.pow(b, 2) + math.pow(c, 2) - math.pow(a, 2)) / (2 * b * c)
if alpha == 0 or beta == 0 or gamma == 0:
    print("100%")
elif alpha < 0 or beta < 0 or gamma < 0:
    print("велика")
else:
    print("крайне мала")