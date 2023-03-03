counter = int(0)
while (name := input()) != "Приехали!":
    if "зайка" in name:
        counter = counter + 1
print(counter)