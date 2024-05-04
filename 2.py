def long(a):
    for i in range(len(a)):
        if len(a[i])>len(a[i-1]):
            print(a[i])
            print(len(a[i]))
a=input().split()
long(a)  


