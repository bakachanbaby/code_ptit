def hangCot(a, n, m):
    dem = n-m
    for i in range(0, n, 2):
        for j in range(m):
            if(dem > 0):
                a[i][j] = -1
            else:
                break
        dem-=1

def Cothang(a, n, m):
    dem = m-n
    for i in range(1, m, 2):
        for j in range(n):
            if(dem > 0):
                a[i][j] = -1
            else:
                break
        dem-=1

s = input().split()
n = int(s[0])
m = int(s[1])
a = []
for i in range(n):
    x = list(map(int, input().split()))
    a.append(x)
if(n > m):
    hangCot(a, n, m)

else:
    Cothang(a, n, m)

for i in range(n):
    flat = False
    for j in range(m):
        if a[i][j] != -1:
            flat = True
            print(a[i][j], end=' ')
    if flat: print()