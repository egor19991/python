x = int(0)
y = int(0)
while (name := input()) != "СТОП":
    change = int(input())
    if name == "СЕВЕР":
        y = y + change
    elif name == "ЮГ":
        y = y - change
    elif name == "ВОСТОК":
        x = x + change
    elif name == "ЗАПАД":
        x = x - change 
print(y)
print(x)