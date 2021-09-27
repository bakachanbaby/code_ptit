t = int(input())
while t > 0:
    t-=1
    n = int(input())
    a = list(map(int,input(). split ()))
    a.sort()
    dem = 1
    flat = True
    for i in range(n-1):
        if(a[i] == a[i+1]):
            dem+=1
        else:
            if(dem % 2 != 0):
                print(a[i])
                flat = False
                break
            else:
                dem = 1
    if(dem % 2 != 0 and flat):
        print(a[n-1])