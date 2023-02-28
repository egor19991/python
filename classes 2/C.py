petya = int(input())
vasya = int(input())
tolya = int(input())
if petya > vasya and petya > tolya:
    print("1. Петя")
elif vasya > petya and vasya > tolya:
    print("1. Вася") 
else:
    print("1. Толя")

if (petya > vasya and petya < tolya) or ((petya < vasya and petya > tolya)):
    print("2. Петя")
elif (vasya > petya and vasya < tolya) or (vasya < petya and vasya > tolya):
    print("2. Вася") 
else:
    print("2. Толя")

if petya < vasya and petya < tolya:
    print("3. Петя")
elif vasya < petya and vasya < tolya:
    print("3. Вася") 
else:
    print("3. Толя")