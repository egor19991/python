import math

def func(number):
    counter = int(0)

    if number > 10:
        for i in range(1, int(math.sqrt(number))):
            if number % i == 0:
                counter = counter + 1
            if counter > 1:
                break
    elif number <= 10:
        for i in range(1, number):
            if number % i == 0:
                counter = counter + 1
            if counter > 1:
                break
    if counter == 1:
        return(True)
    elif number == 1:
        return(False)
    else:
        return(False)


number = int(input())
delete = 2
output = ""
while number > 1:
    if number % delete == 0:
        if output == "":
            output = output + f"{delete}"
        else:
            output = output + f" * {delete}"
        number = number // delete
    elif delete == 2 and number % 2 != 0:
        delete = delete + 1
    else:
        while func(delete) == False:
            delete = delete + 1