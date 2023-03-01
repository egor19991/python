petya = int(input())
vasya = int(input())
tolya = int(input())

if petya > vasya and petya > tolya:
    print("Петя".center(24))
elif vasya > petya and vasya > tolya:
    print("Вася".center(24)) 
else:
    print("Толя".center(24))

if (petya > vasya and petya < tolya) or ((petya < vasya and petya > tolya)):
    print("Петя".center(8))
elif (vasya > petya and vasya < tolya) or (vasya < petya and vasya > tolya):
    print("Вася".center(8)) 
else:
    print("Толя".center(8))

if petya < vasya and petya < tolya:
    print("Петя".center(40))
elif vasya < petya and vasya < tolya:
    print("Вася".center(40)) 
else:
    print("Толя".center(40))

print("   II      I      III   ") 