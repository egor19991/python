numbers = int(input())
sum_numbers = 0
for i in range(0, numbers):
    rabbit = False
    while (animals := input()) != "ВСЁ":
        if animals == "зайка":
            rabbit = True
    if rabbit:
        sum_numbers = sum_numbers + 1
print(sum_numbers)