t = int(input())
while t > 0:
    n = int(input())
    a = []
    for i in range(n):
        x = int(input())
        a.append(x)
    a.sort()
    dem = a.count(a[0])
    b = a[0]
    for i in range(len(a)):
        if(dem < a.count(a[i])):
            dem = a.count(a[i])
            b = a[i]
    print(b)
    t-=1