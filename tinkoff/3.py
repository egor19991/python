length = int(input())
str = input()
min_length = length
for i in range(length):
    for j in range(i, length):
        find_string = str[i : j]
        if (find_string in str) and ("a" in find_string) and ("b" in find_string) and ("c" in find_string) and ("d" in find_string) and min_length > len(find_string):
            min_length = len(find_string)
if min_length == length:
    print("-1")
else:
    print(min_length)
#find_strings.find(str[i : j])