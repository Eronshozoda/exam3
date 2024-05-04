number = input().split()
number.sort()
for i in range(len(number)):
    if int(number[i])%2!=0:
        print((number[i]))
        break
else:
    print(0)