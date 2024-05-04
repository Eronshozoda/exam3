
numbers = input().split()


count_dict = {}


for num in numbers:
    count_dict[num] = count_dict.get(num, 0) + 1


for num in numbers:
    if count_dict[num] == 1:
        print(num, end=" ")  
